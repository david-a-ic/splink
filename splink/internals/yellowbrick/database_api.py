"""
Yellowbrick backend for Splink (scaffold).

This is intentionally a *thin* subclass over the Postgres backend since
Yellowbrick implements the PostgreSQL front-end. We override a few dialect
details and provide a sensible default SQLAlchemy URL scheme.

Notes:
- Requires: `sqlalchemy` and a Postgres driver (typically `psycopg2-binary`).
- You can pass either a SQLAlchemy Engine/Connection or a DSN string.
- This scaffold is designed to live under `splink/internals/yellowbrick/` and
  a public shim at `splink/backends/yellowbrick.py`.
"""
from __future__ import annotations

import warnings
from typing import Any, Optional, Union

try:
    # Prefer importing the Postgres backend from Splink, and subclass it.
    from splink.internals.postgres.database_api import PostgresAPI
except Exception as e:  # pragma: no cover
    raise ImportError(
        "Could not import PostgresAPI. Ensure Splink's Postgres backend is available."
    ) from e

try:
    from sqlalchemy.engine import Engine, Connection
    from sqlalchemy import create_engine, text
except Exception as e:  # pragma: no cover
    raise ImportError(
        "sqlalchemy is required for the Yellowbrick backend"
    ) from e

SQLALCHEMY_SCHEME_DEFAULT = "postgresql+psycopg2"


class YellowbrickAPI(PostgresAPI):
    """Backend API for executing Splink SQL on Yellowbrick Data appliances.

    Because Yellowbrick speaks PostgreSQL on the wire, we reuse nearly all
    functionality of the Postgres backend, only customising small pieces that
    differ in practice (e.g., temp table semantics, some function mappings).
    """

    backend_name = "yellowbrick"
    pretty_name = "Yellowbrick (PostgreSQL-compatible)"
    sqlalchemy_scheme = SQLALCHEMY_SCHEME_DEFAULT

    # Some Yellowbrick-specific toggles (adjust if needed for your appliance/version)
    supports_cte_in_create_view = True
    supports_temporary_tables = True  # YB supports TEMP tables per session
    temp_table_prefix = "tmp_splink_"

    def __init__(
        self,
        connection: Optional[Union["Engine", "Connection", str]] = None,
        *,
        create_engine_kwargs: Optional[dict[str, Any]] = None,
        sql_dialect: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Create a YellowbrickAPI.

        Parameters
        ----------
        connection:
            - SQLAlchemy Engine or Connection; OR
            - DSN string (e.g., 'postgresql+psycopg2://user:pass@host:5432/db')
              If omitted, falls back to env vars or PostgresAPI defaults.
        create_engine_kwargs:
            Extra kwargs forwarded to sqlalchemy.create_engine if `connection`
            is a string.
        sql_dialect:
            Optional override for Splink internal SQL dialect name. Defaults
            to 'yellowbrick' (falls back to Postgres Jinja templates where not overridden).
        **kwargs:
            Forwarded to PostgresAPI.__init__.
        """
        if sql_dialect is None:
            sql_dialect = self.backend_name

        if isinstance(connection, str):
            scheme = connection.split(":", 1)[0]
            if "+" not in scheme and not scheme.startswith("postgresql"):
                warnings.warn(
                    "Connection string does not include a driver; defaulting to "
                    f"{self.sqlalchemy_scheme}.",
                    stacklevel=2,
                )
                connection = f"{self.sqlalchemy_scheme}://{connection}"

        if isinstance(connection, str):
            eng = create_engine(connection, **(create_engine_kwargs or {}))
        else:
            eng = connection  # Engine or Connection or None
        super().__init__(eng, sql_dialect=sql_dialect, **kwargs)

    # --- Optional overrides -----------------------------------------------------------------
    def _version_string(self) -> str:
        """Return Yellowbrick server version string for logging/diagnostics."""
        try:
            with self.engine.connect() as conn:
                # Yellowbrick accepts SELECT version();
                res = conn.execute(text("SELECT version();")).scalar()
                return str(res)
        except Exception:  # fallback to parent implementation
            return super()._version_string()

    @property
    def jinja_base_module(self) -> str:
        """Point Splink to Yellowbrick-specific Jinja macros, falling back to Postgres."""
        # This module provides overrides in splink/internals/yellowbrick/sql/macros.sql.jinja
        return "splink.internals.yellowbrick.sql"

    # If the parent PostgresAPI ever references a 'dialect' object for type coercions
    # or function mappings, you can override/extend them here. For now we lean on
    # Postgres behaviour which generally works on Yellowbrick.

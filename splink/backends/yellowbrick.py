# Thin public shim so users can `from splink import YellowbrickAPI`
# Mirrors pattern used by other backends (e.g., DuckDB, Postgres).
from splink.internals.yellowbrick.database_api import YellowbrickAPI

__all__ = ["YellowbrickAPI"]

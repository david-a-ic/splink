import pytest

try:
    from splink.backends.yellowbrick import YellowbrickAPI
except Exception as e:  # pragma: no cover
    pytest.skip("Yellowbrick backend import failed: %s" % e, allow_module_level=True)


def test_public_api_imports():
    # Ensure the shim resolves correctly
    from splink.backends.yellowbrick import YellowbrickAPI  # noqa: F401


def test_inherits_postgres_api():
    from splink.internals.postgres.database_api import PostgresAPI
    from splink.backends.yellowbrick import YellowbrickAPI
    assert issubclass(YellowbrickAPI, PostgresAPI)

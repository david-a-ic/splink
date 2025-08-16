import os
from splink.backends.yellowbrick import YellowbrickAPI

# Tip: set this in Run/Debug Configurations → Environment variables
dsn = os.getenv("YB_DSN", "postgresql://user:pass@host:5432/dbname")

db = YellowbrickAPI(dsn)

print("Server version:", db._version_string())

# Minimal round-trip: temp table, select a value
with db.engine.connect() as conn:
    conn.execute("create temporary table tmp_splink_test on commit preserve rows as select 1 as x")
    res = conn.execute("select count(*) from tmp_splink_test").scalar()
    print("Temp row count:", res)

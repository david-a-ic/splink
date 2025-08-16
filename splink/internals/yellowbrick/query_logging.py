# Reuse Postgres query logging; customize prefix
from splink.internals.postgres.query_logging import *  # noqa: F401,F403
YB_LOG_PREFIX = "[SPLINK][YELLOWBRICK]"

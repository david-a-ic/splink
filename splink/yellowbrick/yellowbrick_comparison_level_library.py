import warnings

from ..exceptions import SplinkDeprecated
from .comparison_level_library import *  # noqa: F403

warnings.warn(
    "Importing directly from `splink.yellowbrick.yellowbrick_comparison_level_library` "
    "is deprecated and will be removed in Splink v4. "
    "Please import from `splink.yellowbrick.comparison_level_library` going forward.",
    SplinkDeprecated,
    stacklevel=2,
)

import warnings

from ..exceptions import SplinkDeprecated
from .linker import YellowbrickDataFrame, YellowbrickLinker  # noqa: F401

warnings.warn(
    "Importing directly from `splink.yellobrick.linker` "
    "is deprecated and will be removed in Splink v4. "
    "Please import from `splink.yellowbrick.linker` going forward.",
    SplinkDeprecated,
    stacklevel=2,
)

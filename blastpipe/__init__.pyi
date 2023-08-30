"""
This type stub file was generated by pyright.
"""

import platform
import sys
from datetime import date, datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from typing import Annotated, Any, Final

"""blastpipe: A utility library for modern Python."""
__version__ = ...
minor_deprecation = ...
python3_eol = ...
PYMAJOR: Final[int] = ...
PYMINOR: Final[int] = ...
PYPATCH: Final[int] = ...

if datetime.now(tz=timezone.utc).date() > python3_eol:  # type: ignore[operator]
    ...

def public(obj: Any) -> Annotated[Any, '__all__.__contains__(__name__)']:
    """Declares an object as public."""
    ...



"""Import models in a safe order to ensure SQLModel/SQLAlchemy can inspect link models.

This module imports the association/link table first (`news_tag`) so that
`NewsTag` is registered before `News` and `Tag` define relationships that
reference it by string. Importing `backend.models` early (for example in
`main.py`) will ensure models are mapped correctly and avoid NoInspectionAvailable
errors at application startup.
"""

# Import the association table first
from . import news_tag  # noqa: F401

# Then import other models
from . import author  # noqa: F401
from . import category  # noqa: F401
from . import comment  # noqa: F401
from . import news  # noqa: F401
from . import tag  # noqa: F401
from . import user  # noqa: F401

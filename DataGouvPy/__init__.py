__title__ = "DataGouvPy"
__author__ = "CROUStillant Développement"
__version__ = "1.0.1"
__description__ = "A Python wrapper for the data.gouv.fr API, providing easy access to public data in France."

__headers__ = {
    "User-Agent": f"DataGouvPy v{__version__} - https://github.com/CROUStillant-Developpement"
}

__baseURL__ = "https://www.data.gouv.fr/api/1"


from .client import DataGouv

# Exceptions
from .exceptions import DataGouvAPIError


__all__ = [
    "__title__",
    "__author__",
    "__version__",
    "__description__",
    "__headers__",
    "__baseURL__",
    "DataGouv",
    "DataGouvAPIError"
]

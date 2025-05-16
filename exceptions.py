class GeometryError(Exception):
    """Base class for geometry-related exceptions"""

    pass


class InvalidShapeError(GeometryError):
    """Raised when shape parameters are invalid"""

    pass


class NegativeValueError(InvalidShapeError):
    """Raised when negative values are provided"""

    pass

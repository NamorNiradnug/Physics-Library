"""Unit class and unit constants."""


import dimension


class Unit:
    """Unit of measurement."""

    def __init__(
            self,
            coefficient: float = 1,
            dim: dimension.Dimension = dimension.SCALAR
    ):
        self.coefficient = coefficient
        self.dim = dim

    def __mul__(self, other):
        return Unit(self.coefficient * other.coefficient, self.dim * other.dim)

    def __imul__(self, other):
        self.coefficient *= other.coefficient
        self.dim *= other.dim
        return self

    def __truediv__(self, other):
        return Unit(self.coefficient / other.coefficient, self.dim / other.dim)

    def __itruediv__(self, other):
        self.coefficient /= other.coefficient
        self.dim /= other.dim
        return self

    def __pow__(self, power):
        return Unit(self.coefficient ** power, self.dim ** power)

    def __ipow__(self, power):
        self.coefficient **= power
        self.dim **= power
        return self

    def __eq__(self, other):
        return self.coefficient == self.coefficient and self.dim == other.dim

    def copy(self):
        """Copy of object."""
        return Unit(self.coefficient, self.dim)


# Base SI units
ONE = Unit()
METER = Unit(1, dimension.LENGTH)
SECOND = Unit(1, dimension.TIME)
KILOGRAM = Unit(1, dimension.MASS)
AMPER = Unit(1, dimension.AMPERAGE)
KELVIN = Unit(1, dimension.TEMPERATURE)

# Derived SI units
HEWTON = Unit(1, dimension.FORCE)
PASCAL = Unit(1, dimension.PRESSURE)
JOULE = Unit(1, dimension.WORK)

"""Main classes of PyPhysics - Physical and VectorPhysical"""

from unit import Unit, ONE
from vector import Vector


def unit_convert(func):
    def wrapper(self, other):
        return func(self, other.to_unit(self.unit))

    return wrapper


def convert_float(func):
    def wrapper(self, other):
        if type(other) in (int, float):
            other = ScalarPhysical(other)
        return func(self, other)

    return wrapper


class ScalarPhysical:
    def __init__(self, value: float = 0, unit: Unit = ONE):
        self.value = value
        self.unit = unit.copy()

    @convert_float
    @unit_convert
    def __add__(self, other):
        return ScalarPhysical(self.value + other.value, self.unit)

    @convert_float
    @unit_convert
    def __iadd__(self, other):
        self.value += other.value
        return self

    @convert_float
    def __mul__(self, other):
        if type(other) == VectorPhysical:
            return other * self
        return ScalarPhysical(self.value * other.value, self.unit * other.unit)

    @convert_float
    def __imul__(self, other):
        self.value *= other.value
        self.unit *= other.unit

    @convert_float
    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return ScalarPhysical(-self.value, self.unit)

    @convert_float
    @unit_convert
    def __sub__(self, other):
        return ScalarPhysical(self.value - other.value, self.unit)

    @convert_float
    @unit_convert
    def __isub__(self, other):
        self.value -= other.value
        return self

    @convert_float
    def __truediv__(self, other):
        return ScalarPhysical(self.value / other.value, self.unit / other.unit)

    @convert_float
    def __itruediv__(self, other):
        self.value /= other.value
        self.unit /= other.unit
        return self

    def __pow__(self, power):
        return ScalarPhysical(self.value ** power, self.unit ** power)

    def __ipow__(self, power):
        self.value **= power
        self.unit **= power

    @convert_float
    @unit_convert
    def __eq__(self, other):
        return self.value == other.value

    def to_unit(self, unit: Unit):
        if self.unit.dimension != unit.dimension:
            raise AttributeError("Bad unit dimension.")
        return ScalarPhysical(self.value * self.unit.coefficient / unit.coefficient, unit)

    def copy(self):
        return ScalarPhysical(self.value, self.unit)


class VectorPhysical:
    def __init__(self, value: Vector = Vector(), unit: Unit = ONE):
        self.value = value
        self.unit = unit

    @unit_convert
    def __add__(self, other):
        return ScalarPhysical(self.value + other.value, self.unit)

    @unit_convert
    def __iadd__(self, other):
        self.value += other.value
        return self

    @convert_float
    def __mul__(self, other: ScalarPhysical):
        return VectorPhysical(self.value * other.value, self.unit * other.unit)

    @convert_float
    def __imul__(self, other: ScalarPhysical):
        self.value *= other.value
        self.unit *= other.unit
        return self

    @convert_float
    def __rmul__(self, other: ScalarPhysical):
        return self * other

    def __neg__(self):
        return VectorPhysical(-self.value, self.unit)

    @unit_convert
    def __sub__(self, other):
        return VectorPhysical(self.value - other.value, self.unit)

    @unit_convert
    def __isub__(self, other):
        self.value -= other.value
        return self

    @convert_float
    def __truediv__(self, other):
        return VectorPhysical(self.value / other.value, self.unit / other.unit)

    @convert_float
    def __itruediv__(self, other):
        self.value /= other.value
        self.unit /= other.unit
        return self

    @unit_convert
    def __eq__(self, other):
        return self.value == other.value

    def to_unit(self, unit: Unit):
        if self.unit.dimension != unit.dimension:
            raise AttributeError("Bad unit dimension.")
        return VectorPhysical(self.value * self.unit.coefficient / unit.coefficient, unit)

    def to_scalar(self) -> ScalarPhysical:
        return ScalarPhysical(self.value.length(), self.unit)

    def x(self) -> ScalarPhysical:
        return ScalarPhysical(self.value.x(), self.unit)

    def y(self) -> ScalarPhysical:
        return ScalarPhysical(self.value.y(), self.unit)

    def z(self) -> ScalarPhysical:
        return ScalarPhysical(self.value.z(), self.unit)

    def x_vector(self):
        return VectorPhysical(self.value.x_vector(), self.unit)

    def y_vector(self):
        return VectorPhysical(self.value.y_vector(), self.unit)

    def z_vector(self):
        return VectorPhysical(self.value.z_vector(), self.unit)


Physical = ScalarPhysical

"""Main classes of PyPhysics - Physical and VectorPhysical"""

from unit import Unit, ONE


def unit_convert(func):
    def wrapper(self, other):
        return func(self, other.to_unit(self.unit))

    return wrapper


class ScalarPhysical:
    def __init__(self, value: float = 0, unit: Unit = ONE):
        self.value = value
        self.unit = unit.copy()

    @unit_convert
    def __add__(self, other):
        return ScalarPhysical(self.value + other.value, self.unit)

    @unit_convert
    def __iadd__(self, other):
        self.value += other.value
        return self

    def __mul__(self, other):
        return ScalarPhysical(self.value * other.value, self.unit * other.unit)

    def __imul__(self, other):
        self.value *= other.value
        self.unit *= other.unit

    def __neg__(self):
        return ScalarPhysical(-self.value, self.unit)

    @unit_convert
    def __sub__(self, other):
        return ScalarPhysical(self.value - other.value, self.unit)

    @unit_convert
    def __isub__(self, other):
        self.value -= other.value
        return self

    def __truediv__(self, other):
        return ScalarPhysical(self.value / other.value, self.unit / other.unit)

    def __itruediv__(self, other):
        self.value /= other.value
        self.unit /= other.unit
        return self

    def __pow__(self, power):
        return ScalarPhysical(self.value ** power, self.unit ** power)

    def __ipow__(self, power):
        self.value **= power
        self.unit **= power

    @unit_convert
    def __eq__(self, other):
        return self.value == other.value

    def to_unit(self, unit: Unit):
        if self.unit.dimension != unit.dimension:
            raise AttributeError("Bad unit dimension.")
        return ScalarPhysical(self.value * self.unit.coefficient / unit.coefficient, unit)

    def copy(self):
        return ScalarPhysical(self.value, self.unit.copy())


class Vector:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.data = [x, y, z]

    def __add__(self, other):
        return Vector(*(self.data[i] + other.data[i] for i in range(3)))

    def __iadd__(self, other):
        for i in range(3):
            self.data += other.data[i]
        return self

    def __mul__(self, coefficient: float):
        return Vector(*(self.data[i] * coefficient for i in range(3)))

    def __imul__(self, coefficient: float):
        for i in range(3):
            self.data[i] *= coefficient
        return self

    def __neg__(self):
        return Vector(*(-self.data[i] for i in range(3)))

    def __sub__(self, other):
        return Vector(*(self.data[i] - other.data[i] for i in range(3)))

    def __isub__(self, other):
        for i in range(3):
            self.data[i] -= other.data[i]
        return self

    def __truediv__(self, coefficient: float):
        return Vector(*(self.data[i] / coefficient for i in range(3)))

    def __itruediv__(self, coefficient: float):
        for i in range(3):
            self.data[i] /= coefficient
        return self

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return f"Vector({self.data[0]}, {self.data[1]}, {self.data[2]})"

    def length(self):
        return sum(self.data[i] ** 2 for i in range(3)) ** 0.5

    def x(self):
        return self.data[0]

    def y(self):
        return self.data[1]

    def z(self):
        return self.data[2]

    def x_vector(self):
        return Vector(self.data[0], 0, 0)

    def y_vector(self):
        return Vector(0, self.data[1], 0)

    def z_vector(self):
        return Vector(0, 0, self.data[2])


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

    def __mul__(self, other: ScalarPhysical):
        return VectorPhysical(self.value * other.value, self.unit * other.unit)

    def __imul__(self, other: ScalarPhysical):
        self.value *= other.value
        self.unit *= other.unit
        return self

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

    def __truediv__(self, other):
        return VectorPhysical(self.value / other.value, self.unit / other.unit)

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

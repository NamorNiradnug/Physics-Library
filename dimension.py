"""Dimension class and dimension constants."""


class Dimension:
    """Physics dimension."""

    def __init__(
            self,
            length: int = 0,
            time: int = 0,
            mass: int = 0,
            amperage: int = 0,
            temperature: int = 0
    ):
        self.data = [
            length,
            time,
            mass,
            amperage,
            temperature
        ]

    def __mul__(self, other):
        return Dimension(
            *(self.data[i] + other.data[i] for i in range(5))
        )

    def __imul__(self, other):
        for i in range(5):
            self.data[i] += other.data[i]
        return self

    def __truediv__(self, other):
        return Dimension(
            *(self.data[i] - other.data[i] for i in range(5))
        )

    def __itruediv__(self, other):
        for i in range(5):
            self.data[i] -= other.data[i]
        return self

    def __pow__(self, power):
        return Dimension(
            *(self.data[i] * power for i in range(5))
        )

    def __ipow__(self, power):
        for i in range(5):
            self.data[i] *= power
        return self

    def __eq__(self, other):
        return self.data == other.data

    def copy(self):
        """Copy of object."""
        return Dimension(*self.data)


# Base dimensions
SCALAR = Dimension()
LENGTH = Dimension(length=1)
TIME = Dimension(time=1)
MASS = Dimension(mass=1)
AMPERAGE = Dimension(amperage=1)
TEMPERATURE = Dimension(temperature=1)

# Derived dimensions
SQUARE = LENGTH ** 2
VOLUME = LENGTH ** 3
VELOCITY = LENGTH / TIME
ACCELERATION = VELOCITY / TIME
FORCE = MASS * ACCELERATION
PRESSURE = FORCE / SQUARE
MOMENTUM = VELOCITY * MASS
WORK = FORCE * LENGTH

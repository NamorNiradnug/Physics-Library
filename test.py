import unittest

#from . import physicslib
from physicslib import __version__
from physicslib import *


class TestCore(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(dimension.ENERGY, Dimension(2, 1, -2))
        self.assertEqual(dimension.PRESSURE * dimension.SQUARE, dimension.FORCE)
        self.assertEqual(dimension.ACCELERATION * dimension.TIME ** 2, dimension.LENGTH)
        self.assertEqual(dimension.MASS / dimension.VOLUME, Dimension(length=-3, mass=1))
        dim = dimension.SCALAR.copy()
        dim /= dimension.SQUARE
        dim *= dimension.FORCE
        dim **= 4
        self.assertEqual(dim ** 0.5, dimension.PRESSURE ** 2)

    def test_unit(self):
        self.assertEqual(unit.NEWTON / unit.KILOGRAM, Unit(1, dimension.ACCELERATION))
        self.assertEqual(unit.PASCAL * unit.METER ** 2, unit.NEWTON)

    def test_vector(self):
        a = Vector(1, 1)
        b = Vector(0.5, 0.25)
        c = Vector(0, 0.5)
        self.assertEqual(a - b * 2, c)
        self.assertEqual(c.length(), 0.5)
        self.assertEqual(a.length(), 2 ** 0.5)
        self.assertEqual(a.cross(c), 0.5)
        self.assertEqual(a.angle_cos(Vector(0, -1)), -1 / 2 ** 0.5)

    def test_physical_1(self):
        a1 = Physical(2, unit.METER / unit.SECOND ** 2)
        g = Physical(-10, unit.METER / unit.SECOND ** 2)
        v0 = Physical(2, unit.METER / unit.SECOND)
        t = Physical(3, unit.SECOND)
        m1 = Physical(3, unit.KILOGRAM)
        f1 = Physical(6, unit.NEWTON)
        f2 = Physical(3, unit.NEWTON)
        self.assertEqual(f2 - f1, -f2)
        self.assertEqual(a1 * m1, f1)
        self.assertNotEqual(f2, f1)
        with self.assertRaises(AttributeError):
            f1 + a1
        self.assertEqual(f2 + f2, f1)
        self.assertEqual(t * v0 + (g * t ** 2) / 2, Physical(-39, unit.METER))
        g /= 2
        self.assertEqual(t * v0 + (g * t ** 2) / 2, Physical(-16.5, unit.METER))

    def test_physical_2(self):
        # simple calculating of air mass in some room
        molar_mass = Physical(29, unit.GRAM / unit.MOLE)
        temp = Physical(300, unit.KELVIN)
        pressure = Physical(1e5, unit.PASCAL)
        room_volume = Physical(20, unit.METER ** 2) * Physical(3, unit.METER)
        self.assertEqual(
            round(room_volume * pressure * molar_mass / (temp * constants.GAS_CONSTANT)),
            Physical(69.758, unit.KILOGRAM)
        )

    def test_vector_physical(self):
        g = VectorPhysical(Vector(0, -10), unit.METER / unit.SECOND ** 2)
        v0 = VectorPhysical(Vector(40, 40), unit.METER / unit.SECOND)
        self.assertEqual(-v0.y(), Physical(-40, unit.METER / unit.SECOND))
        self.assertEqual(g.y(), Physical(-10, unit.METER / unit.SECOND ** 2))
        t = -v0.y() * 2 / g.y()
        self.assertEqual(t, Physical(8, unit.SECOND))
        self.assertEqual(t * v0.x(), Physical(320, unit.METER))
        v1 = v0 + g * t
        s = v0.x_vector() * t
        self.assertEqual(v1, VectorPhysical(Vector(40, -40), unit.METER / unit.SECOND))
        self.assertEqual((v0 + v1) / 2, s / t)

    def test_str_and_repr(self):
        # --Dimension--
        self.assertEqual(repr(dimension.ACCELERATION), "Dimension(1, 0, -2, 0, 0, 0, 0)")
        self.assertEqual(str(dimension.DENSITY), "L\u207B\u00B3M")
        self.assertEqual(str(dimension.ENERGY / dimension.TEMPERATURE), "L\u00B2MT\u207B\u00B2\u0398\u207B\u00B9")
        self.assertEqual(str(dimension.SCALAR), "scalar")
        # --Unit--
        self.assertEqual(repr(unit.NEWTON), "Unit(1, Dimension(1, 1, -2, 0, 0, 0, 0))")
        self.assertEqual(str(unit.JOULE), "m\u00B2kg\u22C5s\u207B\u00B2")
        self.assertEqual(
            str(Unit(1e-2, Dimension(2, 5, 0, 1, -7))),
            "0.01\u22C5m\u00B2kg\u2075A\u22C5K\u207B\u2077"
        )
        self.assertEqual(str(unit.ONE), "scalar_unit")
        # --Vector--
        self.assertEqual(str(Vector(7.0, -9.8, 3)), "Vector(7.0, -9.8, 3)")
        # --ScalarPhysical
        self.assertEqual(
            str(constants.GRAVITATIONAL_CONSTANT),
            "6.674301515\u22C51e-11\u22C5m\u00B3kg\u207B\u00B9s\u207B\u00B2"
        )
        self.assertEqual(str(Physical(9, unit.KILOGRAM)), "9\u22C5kg")
        self.assertEqual(str(Physical(80)), "80")
        # --VectorPhysical--
        self.assertEqual(
            str(VectorPhysical(Vector(0, 9.81), unit.METER * unit.SECOND ** -2)),
            "Vector(0, 9.81, 0)\u22C5m\u22C5s\u207B\u00B2"
        )


if __name__ == "__main__":
    print(f"Testing physicslib v{__version__}")
    unittest.main()

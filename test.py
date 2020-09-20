import unittest

from physicslib import unit, physical, dimension
from physicslib.vector import Vector


class TestCore(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(dimension.WORK, dimension.Dimension(2, 1, -2))
        self.assertEqual(dimension.PRESSURE * dimension.SQUARE, dimension.FORCE)
        self.assertEqual(dimension.ACCELERATION * dimension.TIME ** 2, dimension.LENGTH)
        self.assertEqual(dimension.MASS / dimension.VOLUME, dimension.Dimension(length=-3, mass=1))
        dim = dimension.SCALAR.copy()
        dim /= dimension.SQUARE
        dim *= dimension.FORCE
        dim **= 4
        self.assertEqual(dim ** 0.5, dimension.PRESSURE ** 2)

    def test_unit(self):
        self.assertEqual(unit.NEWTON / unit.KILOGRAM, unit.Unit(1, dimension.ACCELERATION))
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

    def test_physical(self):
        a1 = physical.Physical(2, unit.METER / unit.SECOND ** 2)
        g = physical.Physical(-10, unit.METER / unit.SECOND ** 2)
        v0 = physical.Physical(2, unit.METER / unit.SECOND)
        t = physical.Physical(3, unit.SECOND)
        m1 = physical.Physical(3, unit.KILOGRAM)
        f1 = physical.Physical(6, unit.NEWTON)
        f2 = physical.Physical(3, unit.NEWTON)
        self.assertEqual(f2 - f1, -f2)
        self.assertEqual(a1 * m1, f1)
        self.assertNotEqual(f2, f1)
        with self.assertRaises(AttributeError):
            var = f1 + a1
        self.assertEqual(f2 + f2, f1)
        self.assertEqual(t * v0 + (g * t ** 2) / 2, physical.Physical(-39, unit.METER))
        g /= physical.Physical(2, unit.ONE)
        self.assertEqual(t * v0 + (g * t ** 2) / 2.0, physical.Physical(-16.5, unit.METER))

    def test_vector_physical(self):
        g = physical.VectorPhysical(Vector(0, -10), unit.METER / unit.SECOND ** 2)
        v0 = physical.VectorPhysical(Vector(40, 40), unit.METER / unit.SECOND)
        self.assertEqual(-v0.y(), physical.Physical(-40, unit.METER / unit.SECOND))
        self.assertEqual(g.y(), physical.Physical(-10, unit.METER / unit.SECOND ** 2))
        t = -(v0.y() * 2) / g.y()
        self.assertEqual(t, physical.Physical(8, unit.SECOND))
        self.assertEqual(t * v0.x(), physical.Physical(320, unit.METER))
        v1 = v0 + g * t
        s = v0.x_vector() * t
        self.assertEqual(v1, physical.VectorPhysical(Vector(40, -40), unit.METER / unit.SECOND))
        self.assertEqual((v0 + v1) / 2, s / t)

    def test_str_and_repr(self):
        # --Dimension--
        self.assertEqual(repr(dimension.ACCELERATION), "Dimension(1, 0, -2, 0, 0)")
        self.assertEqual(str(dimension.DENSITY), "L\u207B\u00B3M")
        self.assertEqual(str(dimension.WORK / dimension.TEMPERATURE), "L\u00B2MT\u207B\u00B2\u0398\u207B\u00B9")
        self.assertEqual(str(dimension.SCALAR), "scalar")
        # --Unit--
        self.assertEqual(repr(unit.NEWTON), "Unit(1, Dimension(1, 1, -2, 0, 0))")
        self.assertEqual(str(unit.JOULE), "m\u00B2kg\u22C5s\u207B\u00B2")
        self.assertEqual(
            str(unit.Unit(1e-2, dimension.Dimension(2, 5, 0, 1, -7))),
            "0.01\u22C5m\u00B2kg\u2075A\u22C5K\u207B\u2077"
        )
        self.assertEqual(str(unit.ONE), "scalar_unit")
        # --Vector--
        self.assertEqual(str(Vector(7.0, -9.8, 3)), "Vector(7.0, -9.8, 3)")
        # --ScalarPhysical
        self.assertEqual(str(physical.G), "ScalarPhysical(6.6743, Unit(1e-11, Dimension(3, -1, -2, 0, 0)))")
        # --VectorPhysical--
        self.assertEqual(
            str(physical.EARTH_GRAVITY),
            "VectorPhysical(Vector(0, 9.81, 0), Unit(1.0, Dimension(1, 0, -2, 0, 0)))"
        )


if __name__ == "__main__":
    unittest.main()

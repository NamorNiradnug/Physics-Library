import unittest

import dimension
import unit
import physical
from physical import Vector


class TestCore(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(dimension.WORK, dimension.Dimension(2, -2, 1))
        self.assertEqual(dimension.PRESSURE * dimension.SQUARE, dimension.FORCE)
        self.assertEqual(dimension.ACCELERATION * dimension.TIME ** 2, dimension.LENGTH)
        self.assertEqual(dimension.MASS / dimension.VOLUME, dimension.Dimension(length=-3, mass=1))
        dim = dimension.SCALAR.copy()
        dim /= dimension.SQUARE
        dim *= dimension.FORCE
        dim **= 4
        self.assertEqual(dim ** 0.5, dimension.PRESSURE ** 2)

    def test_unit(self):
        self.assertEqual(unit.HEWTON / unit.KILOGRAM, unit.Unit(1, dimension.ACCELERATION))
        self.assertEqual(unit.PASCAL * unit.METER ** 2, unit.HEWTON)

    def test_vector(self):
        a = Vector(1, 1)
        b = Vector(0.5, 0.25)
        c = Vector(0, 0.5)
        self.assertEqual(a - b * 2, c)
        self.assertEqual(c.length(), 0.5)
        self.assertEqual(a.length(), 2 ** 0.5)

    def test_physical(self):
        a1 = physical.Physical(2, unit.METER / unit.SECOND ** 2)
        g = physical.Physical(-10, unit.METER / unit.SECOND ** 2)
        v0 = physical.Physical(2, unit.METER / unit.SECOND)
        t = physical.Physical(3, unit.SECOND)
        m1 = physical.Physical(3, unit.KILOGRAM)
        f1 = physical.Physical(6, unit.HEWTON)
        f2 = physical.Physical(3, unit.HEWTON)
        self.assertEqual(f2 - f1, -f2)
        self.assertEqual(a1 * m1, f1)
        self.assertNotEqual(f2, f1)
        with self.assertRaises(AttributeError):
            f1 + a1
        self.assertEqual(f2 + f2, f1)
        self.assertEqual(
            t * v0 + (g * t ** 2) / 2,
            physical.Physical(-39, unit.METER),
        )
        g /= physical.Physical(2, unit.ONE)
        self.assertEqual(
            t * v0 + (g * t ** 2) / 2.0,
            physical.Physical(-16.5, unit.METER),
        )

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


if __name__ == "__main__":
    unittest.main()

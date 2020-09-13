import unittest

import dimension
import unit


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


if __name__ == '__main__':
    unittest.main()

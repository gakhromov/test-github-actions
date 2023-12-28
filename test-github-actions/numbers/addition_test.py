import unittest
from numbers.addition import add_floats, add_integers


class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_integers(1, 1), 2)
        self.assertEqual(add_floats(1.0, 1.0), 2.0)


if __name__ == '__main__':
    unittest.main()

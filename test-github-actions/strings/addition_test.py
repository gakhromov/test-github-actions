import unittest
from strings.addition import add_strings


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings('Hello', ' World'), 'Hello World')


if __name__ == '__main__':
    unittest.main()

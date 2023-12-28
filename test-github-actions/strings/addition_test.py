import unittest
from strings.addition import add_strings


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings('Hello', ' World'), 'Hello World')

    def test_add_empty_string(self):
        with self.assertRaises(ValueError):
            add_strings('', 'Test again')


if __name__ == '__main__':
    unittest.main()

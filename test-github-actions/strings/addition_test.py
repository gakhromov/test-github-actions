import unittest
from strings.addition import add_strings


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        self.assertEqual(add_strings('Hello', ' World'), 'Hello World')

    def test_add_strings_formatted(self):
        self.assertEqual(add_strings('Hello', f' {50}'), 'Hello 50')


if __name__ == '__main__':
    unittest.main()

from absl.testing import absltest, parameterized
from numbers.addition import add_floats, add_integers


class TestAddition(parameterized.TestCase):

    @parameterized.parameters((1, 1, 2), (5, 6, 11))
    def test_addition(self, a, b, c):
        self.assertEqual(add_integers(a, b), c)
        self.assertEqual(add_floats(float(a), float(b)), float(c))


if __name__ == '__main__':
    absltest.main()

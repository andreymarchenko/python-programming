import unittest
from Polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_init_correct_args(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coefs, [1, 2, 3])

    def test_init_empty_list(self):
        self.assertRaises(Exception, Polynomial, [])

    def test_init_incorrect_list(self):
        self.assertRaises(Exception, Polynomial, ["1", 2])

    def test_init_float_values(self):
        p = Polynomial([1.0, 2.0, 3.0])
        self.assertEqual(p.coefs, [1.0, 2.0, 3.0])

    def test_eq_true(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        self.assertFalse(p1 == p2)

    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [2, 4])

    def test_add_different_polyn_size(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [1, 3, 5])

    def test_add_negative_values(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 1])
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [0, 0])

    def test_add_zero_values(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([0, 0])
        p3 = p1 + p2
        self.assertEqual(p3.coefs, p1.coefs)

    def test_add_positive_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [1, 3])

    def test_add_negative_constant(self):
        p1 = Polynomial([1, 2])
        p2 = -1
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [1, 1])

    def test_add_zero_constant(self):
        p1 = Polynomial([1,2])
        p2 = 0
        p3 = p1 + p2
        self.assertEqual(p3.coefs, p1.coefs)

    def test_add_positive_float_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 2.4
        p3 = p1 + p2
        self.assertEqual(p3.coefs, [1, 4.4])

    def test_mul_same_polyn_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [1, 2, 1])

    def test_mul_different_polyn_size(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [1, 2, 2, 1])

    def test_mul_negative_values(self):
        p1 = Polynomial([1, -1, 1])
        p2 = Polynomial([-1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [-1, 2, -2, 1])

    def test_mul_zero_values(self):
        p1 = Polynomial([1, -1, 1])
        p2 = Polynomial([0, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [0, 0, 0, 0])

    def test_mul_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [0, 0])

    def test_mul_zero_float_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0.0
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [0.0, 0.0])

    def test_mul_float_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 5.4
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [5.4, 10.8])

    def test_mul_one_value_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 * p2
        self.assertEqual(p3.coefs, p1.coefs)

    def test_mul_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 5
        p3 = p1 * p2
        self.assertEqual(p3.coefs, [5, 10])

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(Exception, p1.__mul__, "5")

    def test_str(self):
        p1 = Polynomial([2, 4])
        self.assertEqual(str(p1), '2x+4')

    def test_str_zero_values(self):
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), '0')

    def test_str_first_value_is_zero(self):
        p1 = Polynomial([0, 2, 3])
        self.assertEqual(str(p1), '2x+3')

    def test_str_first_value_is_one(self):
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(str(p1), 'x2+2x+3')

    def test_str_all_values_are_one(self):
        p1 = Polynomial([1, 1, 1])
        self.assertEqual(str(p1), 'x2+x+1')

    def test_str_last_value_is_zero(self):
        p1 = Polynomial([1, 2, 0])
        self.assertEqual(str(p1), 'x2+2x')

    def test_str_first_two_value_is_zero(self):
        p1 = Polynomial([0, 0, 1])
        self.assertEqual(str(p1), '1')

    def test_str_one_value_is_zero(self):
        p1 = Polynomial([0, 1, 0])
        self.assertEqual(str(p1), 'x')

    def test_str_first_value_is_negative(self):
        p1 = Polynomial([-1, 1, 0])
        self.assertEqual(str(p1), '-x2+x')

if __name__ == "__main__":
    unittest.main()
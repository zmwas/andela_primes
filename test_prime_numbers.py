import unittest
from prime_numbers import generate_prime_numbers

class PrimeNumbersTestCase(unittest.TestCase):

    def test_input_is_integer(self):
        with self.assertRaises(TypeError):
             generate_prime_numbers('string')

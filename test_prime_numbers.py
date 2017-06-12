import unittest
from prime_numbers import generate_prime_numbers

class PrimeNumbersTestCase(unittest.TestCase):

    def test_input_is_integer(self):
        with self.assertRaises(TypeError):
             generate_prime_numbers('string')
    def test_ouput_is_list(self):
        result = generate_prime_numbers(10)
        self.assertTrue(type(result) == list,msg="output is not a list")

    

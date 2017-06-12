import unittest
from prime_numbers import generate_prime_numbers

class PrimeNumbersTestCase(unittest.TestCase):

    def test_input_is_integer(self):
        with self.assertRaises(TypeError):
             generate_prime_numbers('string')
    def test_ouput_is_list(self):
        result = generate_prime_numbers(10)
        self.assertTrue(type(result) == list,msg="output is not a list")

    def test_output_is_prime(self):
        result =generate_prime_numbers(10)
        self.assertEqual(result,[2,3,5,7],msg="output is not prime")

    def test_output_not_empty(self):
        result = generate_prime_numbers(10)
        self.assertTrue(result!=None)
    def test_output_positive(self):
        result = generate_prime_numbers(10)
        for i in result:
            self.assertTrue(i>0)

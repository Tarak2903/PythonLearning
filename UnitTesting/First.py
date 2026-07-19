from unittest import TestCase

def divide(a,b):
    if b==0:
        raise ValueError("You cannot divide by zero")
    return a/b

class HElo(TestCase):
    def test_divide_result(self):
        a=9
        b=3
        expected_result=3.0
        self.assertEqual(divide(a,b),expected_result)

    def test_divide_result_zero(self):
        with self.assertRaises(ValueError):
            divide(24,0)

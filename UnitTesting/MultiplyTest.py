from unittest import TestCase

def multiply(*args):
    if len(args)==0:
        raise ValueError("YOu cannot multiply 0 times")

    else:
        mul = 1
        for i in args:
            mul*=i
    return mul

class MultiplyTesting(TestCase):
    def test_zero_argument(self):
        with self.assertRaises(ValueError):
            multiply()


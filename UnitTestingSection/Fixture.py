import pytest


class Calculator:
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b

@pytest.fixture()
def calc():
    return Calculator()



def test_multiplication(calc):

    assert (calc.multiply(2,3),6)

def test_division(calc):
    assert (calc.divide(6,2),3.0)
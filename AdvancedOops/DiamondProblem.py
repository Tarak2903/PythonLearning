class A:
    def __init__(self):
        print("A i am ")
class B(A):
    def __init__(self):
        print("B i am ")
        super().__init__()

class C(A):
    def __init__(self):
        print("C i am")
        super().__init__()

class D(C,B):
    def __init__(self):
        print("D i am")
        super().__init__()

d=D()

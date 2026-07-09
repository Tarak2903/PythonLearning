class DivideZeroError(TypeError):
    def __init__(self,msg):
        super().__init__(msg)



def divide(a,b):
    if b==0:
        raise DivideZeroError("You cannot divide by Zero")
    return a/b


try:
    print(divide(1,0))
except DivideZeroError:
    print("You cannot divide by 0")
finally:
    print("COmpleted")


def divide(a,b):
    if b==0:
        raise ZeroDivisionError('Division by zero')
    return a/b

print(divide(2,3))

class CustomError(TypeError):
    pass

raise CustomError()
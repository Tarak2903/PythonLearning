
def decorator_function(original_function):
    def wrapper_function(*args):
        print("Logging the values")
        original_function(*args)
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")
@decorator_function
def display1(name,age):
    print(f"My name is {name} and my age is {age}")
display()
display1("Tarak",13)

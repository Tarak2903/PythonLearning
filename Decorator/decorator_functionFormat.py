

def hello_function(original_function):
    def wrapper_function():
        print(f"This is running before the {original_function.__name__}")
        return original_function()
    return wrapper_function

@hello_function
def display():
    print("Hello world")

display()
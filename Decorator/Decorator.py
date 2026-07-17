def display():
    print("Display function ran")

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

decorated_display=decorator_function(display)
decorated_display()

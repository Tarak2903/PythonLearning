class DecoratorClass:
    def __init__(self,original_function):
        self.original_function=original_function
    def __call__(self, *args, **kwargs):
        print(f"This method is called before {self.original_function}")
        return self.original_function(*args,*kwargs)
@DecoratorClass
def display(name, age):
    print(f"Display function ran {name} and age is {age}")

display("Tarka",12)
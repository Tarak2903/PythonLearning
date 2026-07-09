class Student:
    def show(self):
        print("Hello World")

s=Student()
print(s.show)



'''
Bound Method Stores 2 things ->
1. Object
2. Function


Bound methods can be stored in variables and can be used passed as parameter also


Bound methods are done using something like Student.__dict__["show"].__get__(s,Student) internally
'''
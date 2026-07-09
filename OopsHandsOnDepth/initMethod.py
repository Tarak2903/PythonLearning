#How is self attached to a method?
#Python binds the object  to a method

class Student:
    def show(self):
        print(self)

s= Student()
s.show()

Student.show(s)

'''
IMPORTANT __init__  RUNS FOR OBJECT INITIALIZATION AFTER OBJECT CREATION

It is not declaration
It is simply runtime attribute assignment.
Its return type in NONE




<__main__.Student object at 0x772c636a34d0>
<__main__.Student object at 0x772c636a34d0>

Both show exactly the same output


Self refers to the current instance
'''
#Python can create attributes at runtime


class Student:
    pass

s= Student()

s.name="Tarak"
s.age=21

print(s.__dict__)
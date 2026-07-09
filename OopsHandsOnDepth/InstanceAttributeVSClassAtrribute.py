class Student:
    college="CU"

s1= Student()
s2=Student()

s1.name="Tarak"
s2.name="keshav"

print(s1.__dict__)
print(Student.__dict__)

#There can also be the concept of attribute shadowing where in you can overshadow the parameter using the  s.college=CGC
#Class attribute can be deleted as well using the del keyword
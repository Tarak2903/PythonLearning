
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average(self):
        return sum(self.grades)/len(self.grades)

MyStudent =Student("James",[10,20,30,40])
print(MyStudent.average())



# This also works

print(Student.average(MyStudent))



#-------------------------Magic Methods----------------------------------------------

class Garage:
    def __init__(self,name,cars):
        self.name=name
        self.cars=cars
    def __str__(self):
        return f'This is a Garage with {len(self.cars)} cars'
    def __getitem__(self,index):
        return self.cars[index]



#Important Note repr is something which can be used to recreate an Object real example is DateTime
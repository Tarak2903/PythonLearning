class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        return sum(self.marks)/len(self.marks)
class WorkingStudent(Student):
    def __init__(self,name,marks,salary):
        super().__init__(name,marks)
        self.salary = salary
#Note without super also it works

ws=WorkingStudent('Tarak',[100,200,300],100)
print(ws.avg())


#class name of function is function only1


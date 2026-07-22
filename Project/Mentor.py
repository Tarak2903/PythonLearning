from Project.Intern import Intern
from Project.Intern import Course
class Mentor:

    def __init__(self,name):
        self.name=name
        self.interns=[]
        self.courses_available=[]

    def add_intern(self):
        intern_name=input("Enter name of the inter -> ")
        intern=Intern(intern_name)
        self.interns.append(intern)

    def add_course(self):
        course_name=input("Enter the name of course please -> ")
        course_total_sections=int(input("Enter the total sections of the course -> "))
        course=Course(course_name,course_total_sections)
        self.courses_available.append(course)
        print("Course added successfully!!\n")

    def list_available_course(self):
        if len(self.courses_available)==0:
            print("No course added Please add some course")
        else:

            for course in self.courses_available:
                print(f"{course.course_name_getter()}")

    def assign_course(self):
        if len(self.courses_available)==0:
            print("No course added Please add some course to assign Course\n")
        else:
            print("Please enter the name of course from the following courses to assign course to intern ")
            self.list_available_course()
            course_name=input()
            for course in self.courses_available:
                if course.course_name_getter().lower()==course_name:
                    assigned_course=course
                    for intern in self.interns:
                        intern.add_course(assigned_course)
                        print("Course Added Successfully!!")
                    break

            else:
                raise ValueError("Wrong course name added")



    def list_interns(self):
        if len(self.interns)==0:
            print("No interns are assigned to you")
        else:
            print("Following are the interns that are assigned to you -> \n")
            for intern in self.interns:
                print(f"{intern.intern_name_getter()}")

    def check_intern_status(self):
        intern_name=input("Enter the name of intern to check their status -> ")
        for intern in self.interns:
            if intern.intern_name_getter()==intern_name:
                self.check_particular_intern(intern)
                break

        else:
            raise ValueError("Intern not found")


    def check_particular_intern(self,intern):
        intern.complete_intern_detail()



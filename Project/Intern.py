from Project.Course import Course

class Intern:
    def __init__(self,name):
        self.name=name
        self.course_assigned=[]

    def intern_name_getter(self):
        return self.name

    def check_course_status(self,name):
          pass

    def list_all_courses(self):
        for c in self.course_assigned:
            print(f'''Course name -> {c.name}
                    Progress -> {c.calculate_completion_percentage()}''')

    def complete_current_section(self,):
        pass

    def add_course(self,course):
        self.course_assigned.append(course)

    def complete_intern_detail(self):
        print(f"Intern name -> {self.name}\nTotal Courses assigned -> {len(self.course_assigned)}")

        if len(self.course_assigned)==0:
            print("Course Status unavailable No courses assigned yet")
        else:
            for course in self.course_assigned:
                print(f"Course Name -> {course.course_name_getter()}\nProgress -> {course.calculate_completion_percentage()}%")




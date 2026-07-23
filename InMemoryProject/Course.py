class Course:
    def __init__(self,name,total_section):
        self.name=name
        self.total_section=total_section
        self.completed_section=0

    def complete_current_section(self)->None:
        self.completed_section+=1

    def calculate_completion_percentage(self)->float:
        return self.completed_section/self.total_section

    def course_name_getter(self)->str:
        return self.name




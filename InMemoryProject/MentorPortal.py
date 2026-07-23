from InMemoryProject.Mentor import  Mentor
m=Mentor("xyz")

mentor_prompt='''
Welcome please select from the following options
1 -> Add Course
2 -> Add intern
3 -> View Interns
4 -> Check Intern Status
5 -> Assign added course
6 -> View Added Courses
7 -> Quit

'''

mentor_input=None
while mentor_input!=6:
    mentor_input = int(input(mentor_prompt))
    if mentor_input == 1:
        m.add_course()
    elif mentor_input == 2:
        m.add_intern()
    elif mentor_input == 3:
        m.list_interns()
    elif mentor_input == 4:
        m.check_intern_status()
    elif mentor_input == 5:
        m.assign_course()
    elif mentor_input == 6:
        m.list_available_course()
    elif mentor_input == 7:
        print("Thank you!")
        break
    else:
        print("Invalid Choice\n")
    mentor_input = int(input(mentor_prompt))
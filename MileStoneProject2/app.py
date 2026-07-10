from utils import database

user_choice="""
ENTER-
a: to add new book
l: to list all books
r: to mark a book as read
d: to delete a book
q: to quit

"""

def menu():
    user_input=input(user_choice)
    while user_input!='q':
        if user_input=='a':
            database.add_book()
        elif user_input=='l':
            database.list_book()
        elif user_input=='r':
            database.read_book()
        elif user_input=='d':
            database.delete_book()
        elif user_input=='q':
            break
        else :
            print("Invalid choice")
        user_input = input(user_choice)


menu()
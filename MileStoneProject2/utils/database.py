ls = []


def add_book():
    bookname = input("Enter the name of the book: ")
    book_author = input("Enter the author of the book: ")

    ls.append({
        "name": bookname,
        "author": book_author,
        "read": False
    })

    print("Book added Successfully!")


def list_book():
    print(ls)


def delete_book():
    global ls

    book = input("Enter the name of book to be deleted: ")

    ls = [l for l in ls if l["name"] != book]

    print("Book deleted successfully")


def read_book():
    book = input("Enter the name of book to be read: ")

    for i in range(len(ls)):
        if ls[i]["name"] == book:
            print("Hello world")
            ls[i]["read"] = True
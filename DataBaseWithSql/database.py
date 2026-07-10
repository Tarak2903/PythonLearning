import  sqlite3
from multiprocessing import connection


def create_book_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute("create table books(name text primary key ,author text,read integer)")

    connection.commit()
    connection.close()

def add_book(author,name):
    connection1=sqlite3.connect('data.db')
    cursor =connection1.cursor()
    cursor.execute("insert into books values (?,?,0) ",(name,author))

    connection1.commit()
    connection1.close()

def get_book():
    connection2=sqlite3.connect('data.db')
    cursor=connection2.cursor()
    cursor.execute("select * from books")
    books=cursor.fetchall()
    books= [{"name":row[0],"author":row[1],"read":row[2]} for row in books]
    connection2.commit()
    connection2.close()
    print(books)
    return books

def delete_book(name):
    connection3= sqlite3.connect('data.db')
    cursor=connection3.cursor()
    cursor.execute("delete from  books where name=?",(name,))
    connection3.commit()
    connection3.close()
def mark_as_read(name):
    connection4=sqlite3.connect('data.db')
    cursor=connection4.cursor()

    cursor.execute("update books set read = 1 where name=?",(name,))
    connection4.commit()
    connection4.close()

# delete_book("rowling")
get_book()
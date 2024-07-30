import sqlite3

my_database="library2.db"

con = sqlite3.connect("library2.db")

con.execute( 'create table if not exists book( book_id text primary key, title text, author text, status text )' ) 
con.execute( 'create table if not exists book_issued( book_id text primary key, book_name text, issue_to text, rollno int, semester text, section text, branch text, issue_date date )' ) 

con.commit()
con.close()

BookTable = "book"
IssueTable = "book_issued"

def add_book():
    allBid = []
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    status = "Available"
    con = sqlite3.connect("library2.db")
    getbid = "select book_id from book" 
    Extract_Book_Id = con.execute(getbid)
    con.commit()
    for i in Extract_Book_Id:
        allBid.append(i[0])
    if book_id in allBid:
        print("\nBook ID Already Exists Choose Unique Book id\n")
    else:    
        con.execute("insert into book values(?,?,?,?)",(book_id,title,author,status))
        con.commit()
        con.close()
        print("Book Added Successfully")
    

def issue_book():
    allBid = []
    allBookId = []
    Issue = "Issued"
    bookId = input("Enter Book ID: ")
    book_name = input("Enter Book Title:")
    name = input("Enter Name: ")
    rollno = int(input("Enter Roll Number: "))
    semester = input("Enter Semester: ")
    section = input("Enter Section: ")
    branch = input("Enter Branch: ")
    date = input("Enter Issue Date(dd-mm-yyyy): ")
    con = sqlite3.connect("library2.db")
    getbid = "select book_id from book_issued" 
    Extract_Book_Id = con.execute(getbid)
    con.commit()
    for i in Extract_Book_Id:
        allBid.append(i[0])
    if bookId in allBid:
        print("\nBook is Already Issued\n")
    else:
        Book_Title = con.execute("select title from book where book_id = ?",(bookId,))
        Book_Title = Book_Title.fetchone()
        con.commit()
        for i in Book_Title:
            check = i
            if check != book_name:
                print("\nBook Title is Incorrect For This Book Id\n")
            else:    
                getBookId = "select book_id from book" 
                Extract_Book_Id = con.execute(getBookId)
                con.commit()
                for i in Extract_Book_Id:
                    allBookId.append(i[0])
                if bookId in allBookId:
                    con = sqlite3.connect("library2.db")
                    Book_Status = con.execute("select status from book where book_id = ?",(bookId,))
                    Book_Status = Book_Status.fetchone()
                    con.commit()
                    for i in Book_Status:
                        check = i
                    if check == 'Available':
                        con.execute("insert into book_issued values(?,?,?,?,?,?,?,?)",(bookId,book_name,name,rollno,semester,section,branch,date))
                        con.execute("update book set status = ? where book_id = ?",(Issue,bookId))
                        con.commit()
                        print("Book Issued Successfully")
                    else:
                        print("Book is already Issued")
                else:
                    print("Book Not Found")
                con.commit()
                con.close()


def return_book():
    book_id_list = []
    Avail = "Available"
    bookId = input("Enter Book ID: ")
    con = sqlite3.connect("library2.db")
    getbid = "select book_id from book_issued"
    Extract_BOOK_id = con.execute(getbid)
    con.commit()
    for i in Extract_BOOK_id:
        book_id_list.append(i[0])
    if bookId in book_id_list:
        con.execute("delete from book_issued where book_id = ?",(bookId,))
        con.execute("update book set status = ? where book_id = ?",(Avail,bookId))
        con.commit()
        print("Book Returned Successfully")
    else:
        print("Book Not Issued or Wrong Book ID")



def display_books():
    
    con = sqlite3.connect("library2.db")
    book_details = con.execute('select * from book')
    con.commit()
    print("\n")
    print("(Book_Id   Title   Author   Status)\n")
    for i in book_details:
        print(i)
    print("\n")



def display_issued_books():
    con = sqlite3.connect("library2.db")
    issued_book_details = con.execute('select * from book_issued')
    con.commit()
    print("\n")
    print("(Book_Id   Book_Name   Issued_to   RollNo   Semester   Section   Branch   Issue_Date)\n")
    for i in issued_book_details:
        print(i)
    print("\n")    


def delete_books():
    allBid = []
    bookId = input("Enter Book ID of the Book to be Deleted: ")
    con = sqlite3.connect("library2.db")
    getbid = "select book_id from book" 
    Extract_Book_Id = con.execute(getbid)
    con.commit()
    for i in Extract_Book_Id:
        allBid.append(i[0])
    if bookId in allBid:
        con = sqlite3.connect("library2.db")
        Book_Status = con.execute("select status from book where book_id = ?",(bookId,))
        Book_Status = Book_Status.fetchone()
        con.commit()
        for i in Book_Status:
            check = i
        if check == "Available":
            con.execute("delete from book where book_id = ?",(bookId,))
            con.commit()
            print("Book Deleted")
        else:
            print("Book is Issued Can't be deleted")



def main():
    print("\n")
    print("WELCOME TO LIBRARY")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Delete Books")
    print("5. Display Books")
    print("6. Display Issued Books")
    print("7. Exit")
    a = int(input("Enter Choice:"))
    if a == 1:
        add_book()
    elif a == 2:
        issue_book()
    elif a == 3:
        return_book()
    elif a == 4:
        delete_books()
    elif a == 5:
        display_books()
    elif a == 6:
        display_issued_books()
    elif a == 7:
        exit()    
    else:
        print("Wrong Choice")

main()


while 1:
    b = input("Do you want to do further operations (y/n): ")
    if b == "y":
        main()
    else:
        exit()    
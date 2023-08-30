from Bookmodel import Book
def print_info(book):
    print(f"ISBN NO:{book.ISBN_num}, Title:{book.title},FORMAT:{book.format},SUBJECT:{book.subject},rental_price_per_day:{book.rental_price},number_of_copies:{book.copies}")

class BookFunction:
    def __init__(self) :
        self.list_of_books = []
        self.initial_data()
    
    def initial_data(self):
        Book1 = Book(ISBN_num ="ISBN0001",title = "photosynthesis",format= "Hardcover", subject ="Science",rental_price = 15.00,copies = 4)
        Book2 = Book(ISBN_num ="ISBN0002", title ="Zoology", format="Paperback", subject ="Science",rental_price = 20.00,copies = 0)
        Book3 = Book(ISBN_num ="ISBN0003",title = "The hitler",format= "Hardcover", subject ="History", rental_price =10.00,copies = 2)
        self.list_of_books.append(Book1)
        self.list_of_books.append(Book2)
        self.list_of_books.append(Book3)

 

    def addfunc(self):
        __isbn = input("Enter ISBN number of the book:").strip().upper()
        __title = input("Enter title of the book:").strip()
        __format = input("Enter format of the book:")
        __subject = input("Enter subject of the book:")
        __rental_price = float(input("Enter rental price per day of the book:"))
        __copies = int(input("Enter number of copies of the book:"))
        Book_New = Book(ISBN_num =__isbn,title = __title,format= __format, subject =__subject,rental_price = __rental_price,copies = __copies)
        self.list_of_books.append(Book_New)
        
        print("Book  added successfully")
        
    def removefunc(self):
        removeBook = input("Enter the ISBN number of the book you want to remove:")
        matched= list(books for books in self.list_of_books if books.ISBN_num == removeBook)
        for books in matched:
            self.list_of_books.remove(books)
        print("Book removed successfully")
        




    def available(self):
        matched = list (books for books in self.list_of_books if books.copies > 0)
        for books in matched:
            print_info(book = books)
        
        
                
            

    def unavailable(self):
        matched = list(books for books in self.list_of_books if books.copies == 0)
        for books in matched:
            print_info(book = books)
        


    def show_all(self):
        for books in self.list_of_books:
            print_info(book = books)
           
        

    def lend(self):
        removeBook = input("Enter the ISBN number: ")
        __copies = int(input("enter lend copies:"))
        matched= list(books for books in self.list_of_books if books.ISBN_num == removeBook)
        for books in matched:
            books.copies -= __copies
        print("Book lent")

    def update_again(self):
        removeBook = input("Enter the ISBN number: ")
        __copies = int(input("enter received copies:"))
        matched= list(books for books in self.list_of_books if books.ISBN_num == removeBook)
        for books in matched:
            books.copies += __copies
        print(f"Book Received with {__copies} copies")
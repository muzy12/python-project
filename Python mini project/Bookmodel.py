class Book:
    def __init__(self,ISBN_num, title, format, subject, rental_price, copies):
        self.ISBN_num = ISBN_num
        self.title= title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies
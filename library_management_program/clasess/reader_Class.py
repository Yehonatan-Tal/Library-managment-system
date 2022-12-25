import datetime
from datetime import date

class Reader():
    def __init__(self):
        self.id = 0
        self.books = []

    def read_book(self, title):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        data = {"Title" : title, "Borrow date" : d1}
        self.books.append(data)

    def print_books_self(self):
        for book in self.books:
            print("\nTitle: " + "'" + book["title"] + "'" + ", Borrow date: " + book["borrow date"] + "\n")   

       
    
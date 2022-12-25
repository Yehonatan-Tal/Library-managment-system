import ctypes

class Shelf():
    def __init__(self):
        self.books = []
        self.is_shelf_full = False

    def add_Book(self, book):
        if len(self.books) < 5:  self.books.append(book) 
        else: print("\nThere is no more space on the shelf!\n")
        if len(self.books) == 5: self.is_shelf_full = True 

    def replace_books(self):
         print("\nSelect the book number whose place you would like to change:\n")
         for book in self.books: print(str(self.books.index(book) + 1) + ": " + book.title)        
         num1 = int(input("\nType your selection here : ")) - 1
         if num1 < len(self.books):
            num2 = int(input("Select the book you want to replace : ")) - 1
            print("\n")
            if num2 < len(self.books):
               self.books[num1] ,self.books[num2] = self.books[num2] ,self.books[num1]
               for book in self.books: print(str(self.books.index(book) + 1) + ": " + book.title)
            else : print("This index does not exist on the shelf!\n")       
         else : print("This index does not exist on the shelf!\n")
    
    def order_books(self):
        for i in range(len(self.books)):
           for j in range(i+1, len(self.books)):
            if self.books[j].num_of_pages < self.books[i].num_of_pages:  self.books[i], self.books[j] = self.books[j], self.books[i]

    def does_shelf_full(self):
        return  self.is_shelf_full

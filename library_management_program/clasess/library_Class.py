from clasess.reader_Class import *

class Library():
    def __init__(self, top, middle, buttom):
        self.shelves = [top, middle, buttom]
        self.readers = []

    def is_there_place_for_new_book(self):
        is_there_place_for_new_book =  False
        for space in self.shelves:
            if space.is_shelf_full == True: None
            else :  is_there_place_for_new_book = True
        print(str(is_there_place_for_new_book))  

    def add_new_book(self, newBook):
        for space in self.shelves:
            if space.is_shelf_full == True: None
            else : 
                space.add_Book(newBook)
                return
 
    def delete_book(self, title):
        Indicator = None
        for shelf in self.shelves:     
           for book in shelf.books:
               if book.title == title:
                  Indicator = True  
                  shelf.books.remove(book)
        if Indicator != True: print("There is no such book by this title on the shelf!\n")
             

    def change_locations(self, firstTitle, secondTitle):
        for shelf in self.shelves:     
            for book in shelf.books:
                if  book.title == firstTitle: first_book = [self.shelves.index(shelf) ,shelf.books.index(book) ,shelf.books.pop(shelf.books.index(book))]
                if  book.title == secondTitle: secound_book = [self.shelves.index(shelf) ,shelf.books.index(book) ,shelf.books.pop(shelf.books.index(book))]            
        self.shelves[first_book[0]].books.insert(first_book[1],secound_book[2])
        self.shelves[secound_book[0]].books.insert(secound_book[1],first_book[2])

        # for books in self.shelves:
        #     print("\nShelf number " + str(self.shelves.index(books)) + ":\n")
        #     books.print_books_data()
               
    def change_locations_in_same_shelf(self, shelf_index):
        self.shelves[shelf_index].replace_books() 
                
    def order_books(self):
        for shelf in self.shelves:
            shelf.order_books() 
                   
    def register_reader(self, id, reader_name):
        reader = Reader()
        reader.id = id
        self.readers.append([reader_name, reader])
                        
    def remove_reader(self, reader_name):
        for reader in self.readers:
            if reader[0] == reader_name: self.readers.pop(self.readers.index(reader))

                            
    def reader_read_book(self, book_title, reader_name):
          for reader in self.readers:
            if reader[0] == reader_name: reader[1].read_book(book_title)
                                
    def search_by_author(self, author_name):       
          for shelf in self.shelves:     
             for book in shelf.books:
                 if  book.author == author_name:
                      print("\n" + "''"+ book.title +"''" + " by " + book.author + "\n")
                 

       
    
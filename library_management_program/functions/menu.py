from clasess.shelf_Class import *
from clasess.book_Class import *
from clasess.reader_Class import *
from clasess.library_Class import *
import json

def menu(library) :
    num = 0
    while(num != 11):
        num = int(input('For adding a book - Press 1.\n'\
                        'For deleting a book - Press 2.\n'\
                        'For changing books locations - Press 3.\n'\
                        'For registering a new reader - Press 4.\n'\
                        'For removing a reader - Press 5.\n'\
                        'For searching books by author – Press 6.\n'\
                        'For reading a book by a reader – Press 7.\n'\
                        'For ordering all books – Press 8.\n'\
                        'For saving all data – Press 9.\n'\
                        'For loading data – Press 10.\n'\
                        'For exit – Press 11.\n'))
        if num == 1:
            newBook = Book() 
            newBook.title = input("")
            newBook.author = input("")
            newBook.num_of_pages = int(input())
            library.add_new_book(newBook)
        if num == 2:
            bookTitle = input("Write the book title you wish to delete : ")
            library.delete_book(bookTitle)
        if num == 3:
            firstTitle = input("Write the title of the book you want to replace : ")
            secondTitle = input("Write the second title you want to replace with the first title : ")
            library.change_locations(firstTitle, secondTitle)
        if num == 4:
            readerName = input("Enter reader name : ")
            readerID = int(input("Enter reader id : "))
            library.register_reader(readerID,readerName)
        if num == 5:
            readerToBeRemove = input("Enter the name of the reader you wish to remove : ")
            library.remove_reader(readerToBeRemove)
        if num == 6:
            author = input("Enter the the author name his books you like to search : ")
            library.search_by_author(author)
        if num == 7:
            readerName = input("Enter reader name : ")
            title = input("Enter book title : ")
            library.reader_read_book(title, readerName)
        if num == 8:
            library.order_books()
    
        if num == 9:
            fileName = input("Enter the file name to save data in : ") + ".json"
            json_data = {"shelves" : [], "readers" : []}
            for shelf in library.shelves :
                books, is_shelf_full = [], shelf.is_shelf_full
                for book in shelf.books :
                    col = {
                            "author" : book.author,
                            "title" :  book.title,
                            "num_of_pages" :  book.num_of_pages
                            }
                    books.append(col)
                shelf_data = {"is_shelf_full" :  is_shelf_full, "books" : books}
                json_data["shelves"].append(shelf_data)
                
            for reader in library.readers :
                books, reader_id = [], reader[1].id
                for book in reader[1].books:
                    col = {
                           "title" : book["Title"],
                           "date" : book["Borrow date"]
                          }     
                    books.append(col)
                readers_data = {"id" : reader_id, "books" : books}
                json_data["readers"].append(readers_data)
            f = open(fileName, "w") 
            data = json.dump(json_data, f)          
            f.close()
        
        if num == 10:
            fileName = input("Enter file name to load data from : ") + ".json"
            f = open(fileName, "r") 
            data = json.load(f)         
            f.close()

        if num == 11: exit
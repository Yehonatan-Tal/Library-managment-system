from clasess.shelf_Class import *
from clasess.book_Class import *
from clasess.reader_Class import *
from clasess.library_Class import *
from flask import request
import requests
from pymongo import MongoClient
from bson import ObjectId
from functions.menu import *


def login():
    print("\nWelcome to the library management system.\nIn order to use the system please log in...\n")
    userName = input("Enter user name : ")
    email = input("Enter email address : ")

    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    users = resp.json()

    check = False
    for user in users:
        if userName == user["username"] and email == user["email"]: check = True

    if check == True: 
        print("\nAccess accepted!\n")
        client = MongoClient(port = 27017)
        db = client["LibraryDB"]
        library_collection = db["library"]
        books = library_collection.find({})
        books = list(books[0:6])
        b1 = Book(books[0]["title"], books[0]["author"] , books[0]["num_of_pages"])
        b2 = Book(books[1]["title"], books[1]["author"] , books[1]["num_of_pages"])
        b3 = Book(books[2]["title"], books[2]["author"] , books[2]["num_of_pages"])
        b4 = Book(books[3]["title"], books[3]["author"] , books[3]["num_of_pages"])
        b5 = Book(books[4]["title"], books[4]["author"] , books[4]["num_of_pages"])
        b6 = Book(books[5]["title"], books[5]["author"] , books[5]["num_of_pages"])

        s1 = Shelf()
        s1.add_Book(b1)
        s1.add_Book(b2)
        s2 = Shelf()
        s2.add_Book(b3)
        s2.add_Book(b4)
        s3 = Shelf()
        s3.add_Book(b5)
        s3.add_Book(b6)
        
        menu(Library(s1, s2, s3))
    
    else: 
        print("\nAccess denied!\n") 
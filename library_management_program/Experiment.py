from clasess.shelf_Class import *
from clasess.book_Class import *
from clasess.reader_Class import *
from clasess.library_Class import *
import ctypes

#Shelf number 0:
a = Book()
a.title = "Harry Potter and the Philosopher's Stone"
a.num_of_pages = 223
a.author = "J. K. Rowling"

b = Book()
b.title = "The Da Vinci Code"
b.num_of_pages = 489 
b.author = "Dan Brown"

c = Book()
c.title = "Fifty Shades of Grey"
c.num_of_pages = 514
c.author = "E. L. James"

d = Book()
d.title = "Angels & Demons"
d.num_of_pages = 768
d.author = "Dan Brown"

e = Book()
e.title = "Twilight"
e.num_of_pages = 498
e.author = "Stephenie Meyer"

#Shelf number 1:
f = Book()
f.title = "The Fault in Our Stars"
f.num_of_pages = 313 
f.author = "John Green"

g = Book()
g.title = "Mockingjay"
g.num_of_pages = 398  
g.author = "Suzanne Collins"

h = Book()
h.title = "Divergent"
h.num_of_pages = 487 
h.author = "Veronica Roth"

i = Book()
i.title = "Gone Girl"
i.num_of_pages = 415 
i.author = "Gillian Flynn"

j = Book()
j.title = "The Martian"
j.num_of_pages = 384 
j.author = "Andy Weir "

#Shelf number 2:
k = Book()
k.title = "All the Light We Cannot See"
k.num_of_pages = 531  
k.author = "Anthony Doerr"

l = Book()
l.title = "Ready Player One"
l.num_of_pages = 374   
l.author = "Ernest Cline"

m = Book()
m.title = "Divergent"
m.num_of_pages = 479  
m.author = "Cassandra Clare"

n = Book()
n.title = "Cinder"
n.num_of_pages = 400  
n.author = "Marissa Meyer"

o = Book()
o.title = "Me Before You"
o.num_of_pages = 369  
o.author = "Jojo Moyes"


s1 = Shelf()
s1.add_Book(a)
s1.add_Book(b)
s1.add_Book(c)
s1.add_Book(d)
s1.add_Book(e)

s2 = Shelf()
s2.add_Book(f)
s2.add_Book(g)
s2.add_Book(h)
s2.add_Book(i)
s2.add_Book(j)

s3 = Shelf()
s3.add_Book(k)
s3.add_Book(l)
s3.add_Book(m)
s3.add_Book(n)
s3.add_Book(o)
    

# E-book is a digital book that can be read using a computer or other electronic devices (electronic book readers).
# Write a program in which define a class that describes states and behaviors of an  e-book.
# Each book has a title, author, number of pages and the current page number that is currently being read.
# It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.

# Place the class describing e-books in a separate file/module. In the main program file, try using the e-book:
import ebook

# a.	Create a book with a title, author, number of pages (check how to set the initial values of the fields at the time
#       of creating the object using the __init__ method / constructor and passing the initial values as arguments to the method call)
book = ebook.Book("Gideon the Ninth", "Tamsyn Muir", 492)

# b.	Open a book
book.open()

# c.	Display a book status (title, author, page numbers, current page no)
book.status()

# d.	Read a few pages
for i in range(5):
    book.read()

# e.	Display a book status
book.status()

# f.	Close a book
book.close()

# g.	Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).
for i in range(5):
    book.read()
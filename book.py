# M4L2 Exercise 1
books = []

import enum
class BookAvailability(enum.Enum):
    available = 1
    borrowed = 2
    

class Book:
    availability = BookAvailability
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = BookAvailability.available
        self._current_user = None
 
    def borrow():
        availability = BookAvailability.borrowed
    
    def return_book():
        availability = BookAvailability.available




class Library:

    def __init__(self, name):
        self.books = []
        self.__name = name


    def add_book(self, title, author, genre, publication_date): 
        book = Book(title, author, genre, publication_date)
        self.books.append(book)


    def search_title(self, title):
        for book in self.books:
            if book.title == title:
                return True
        else:
            return False

    def get_books(self):
        return self.books

# default_book = Book("The Alchemist", "Paulo Coelho", "Fiction", 1988)
# books.append(default_book)

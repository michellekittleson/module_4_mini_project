# M4L2 Exercise 1

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
 
    def borrow(user):
        _current_user = user
        availability = BookAvailability.borrowed
    
    def return_book():
        _current_user = None
        availability = BookAvailability.available


books = []

class Library:

    def __init__(self, books):
        self.__books = books


    def add_book(title, author, genre, publication_date): 
        __books.append(Book({'title': title, 'author': author, 'genre': genre, 'publication date': publication_date}))

    def borrow_book(user, title):
        for book in __books:
            if book.title == title:
                book.borrow(user)
                break
        else:
            return False


    def return_book(title):
        for book in __books:
            if book.title == title:
                book.return_book()
                break
        else:
            return False

    def search_title(title):
        for book in __books:
            if book.title == title:
                return True
        else:
            return False

    def get_books(self):
        return self.__books

# default_book = Book("The Alchemist", "Paulo Coelho", "Fiction", 1988)
# books.append(default_book)

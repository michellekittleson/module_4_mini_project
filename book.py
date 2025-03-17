# M4L2 Exercise 1
# books = []
# authors = []
# users = []

    

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
 
    def borrow(self):
        # If available, set to not available, if not available, set to available
        if self.availability:
            self.availability = False
            return True
        return False
    
    def return_book(self):
        self.availability = True
        





        





# default_book = Book("The Alchemist", "Paulo Coelho", "Fiction", 1988)
# books.append(default_book)






class User:

    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_borrowed_books(self):
        return self.__borrowed_books

    
    def return_book(self, book):
    # Should be checking the library for the books
        if book in self.__borrowed_books:
            book.availability = True
            self.__borrowed_books.remove(book)
        else:
            return False
    
    def borrow_book(self, book):
        if book in self.__borrowed_books:

            return False
        book.availability = False
        # Availability is set here instead of main.py
        self.__borrowed_books.append(book)

        # If book is not in the library
    
    def view_user_details(self):
        return {
            "Name": self.name,
            "Biography": self.biography
        }
from book import Book
from user import User
from author import Author

class Library:

    def __init__(self, name):
        self.books = []
        self.__name = name
        self.borrowed_books = []
        self.authors = []
        self.users = []

    def get_books(self): # New
        if self.books:
            return self.books
        else:
            return "No books in library"

    def add_book(self, title, author, genre, publication_date): 
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
    

    def borrow_book(self, book, user): # new
        if book in self.books: # Check for book in book list
            if book.availability: # check if book is available and rent out
                book.availability = False
                user.borrow_book(book)
                return f"Borrowed book '{book.title}'."
            else:
                return "Book is not available"
        else:
            return "Book not found in library"
    
    def return_book(self, book, user): # To do: Repeat logic in borrow book function but reverse the availability and remove book from user's borrowed books
        if book in self.books:
            if book.availability:
                return "Book has already been returned to the library."
            else:
                book.availability = True
                user.return_book(book)
        

    def search_title(self, title):
        for book in self.books:
            if book.title == title:
                return True
        else:
            return False


    
    def display_authors(self):
        for author in self.authors:
            print(author)
    
    # TODO: Adjust it to take in author object instead of name and biography
    # OR: Create an author object inside the function and append it to the authors list
    # removing the create new_author logic from choice 1 in main.py 
    def add_author(self, author):
        self.authors.append(f"Name: {author.name}, Biography: {author.biography}")
    
    def add_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users.append(new_user)
    
    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def get_user(self, name):
        for user in self.users:
            if name == user.get_name():
                print("Found user")
                return user
        print("No user found")    
        return None # Return None if user not found
    
    def get_users(self):
        for user in self.users:
            print("Found user")
            return user
        print("no user found")
        return None
    
    def display_users(self):
        for user in self.users:
            print(user)
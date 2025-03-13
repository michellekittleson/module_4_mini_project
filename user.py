users = []

class UserManager:
    def __init__(self):
        self.__users = []

    def add_user(self, name, library_id):
        user = User(name, library_id)
        self.users.append(user)

    def get_users(self):
        return self.__users


class User:

    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_borrowed_books(self):
        return self.__borrowed_books

    
    def return_book(title):
    # Should be checking the library for the books
        for book in self.__borrowed_books:
            if book.title == title:
                book.return_book()
                break
        else:
            return False
    
    def borrow_book(self, title):
        for book in self.__borrowed_books:
            if book.title == title:
                return False
        else:
            return False
        # If book is not in the library
    

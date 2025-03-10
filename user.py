

class UserManager:
    def __init__(self):
        self.__users = []

    def add_user():
        # Check if user already exists
        __users.append(User.name)

    def get_users():
        return __users


class User:
    __borrowed_books = []

    def get_borrowed_books(self):
        return self.__borrowed_books

    def __init__(self, name, user_id):
        self.name = name 
        self.user_id = user_id 
        # Library ID?
    
    def borrow_book(self, title):
        for book in self.__borrowed_books:
            if book.title == title:
                return False
        else:
            return False
        # If book is not in the library
    
    def return_book(title):
        for book in __books:
            if book.title == title:
                book.return_book()
                break
        else:
            return False
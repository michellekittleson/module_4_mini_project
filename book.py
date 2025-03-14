# M4L2 Exercise 1
books = []
authors = []
users = []

    

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
        




class Library:

    def __init__(self, name):
        self.books = []
        self.name = name
        self.borrowed_books = []



    def add_book(self, title, author, genre, publication_date): 
        # book = Book(title, author, genre, publication_date)
        # self.books.append(book)
        # self.books.append(Book(title, author, genre, publication_date))
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
    
    # Does this mean I delete these methods from user.py?
    def borrow_book(self, title, user):
        # for book in self.books:
        #     if book.title == title and title not in self.borrowed_books:
        #         self.borrowed_books[title] = user.name
        #         return True
        #     return False
        # Later, Chat GPT says to do this instead
        for book in self.books:
            if book.title == title:
                self.borrowed_books.append((book, user)) # Store book-use pair
                self.books.remove(book)
                return True
            return False # Book not found or already borrowed
    
    def return_book(self, title, user):
        # if title in self.borrowed_books and self.borrowed_books[title] == user.name:
        #     del self.borrowed_books[title]
        #     return True
        # return False
        # Chat GPT now says:
        for pair in self.borrowed_books:
            book, borrower = pair
            if book.title == title and borrower.name == user.name:
                self.books.append(book) # Return book to available books
                self.borrowed_books.remove(pair) # Remove from borrowed books
                return True
        return False # Book not found in borrowed books

    def search_title(self, title):
        for book in self.books:
            if book.title == title:
                return True
        else:
            return False

    def get_books(self):
        return self.books
    
    def display_authors(self):
        for author in authors:
            print(author)
    
    def add_author(self, name, biography):
        name = input("Enter author's name: ")
        biography = input("Enter author's biography: ")
        authors.append(f"Name: {name}, Biography: {biography}")
    
    def add_user(self, name, library_id):
            new_user = User(name, library_id)
            self.users.append(new_user)

    def get_users(self):
        return self.__users
    
    def get_user(self, name):
        # return self.users.get(name, None) # Return user object or None
        # Chat GPT recommendation:
        for user in self.users:
            if user.name == name:
                return user
        return None # Return None if user not found


        





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
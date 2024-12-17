books = []

class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability
   
    def add_book(): 
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        publication_date = input("Enter publication date: ")
        books.append(Book(title, author, genre, publication_date))
 
    def borrow_book():
        title = input("Enter book to borrow: ")
        if title in books:
            book = books[title]
            if book.availability == True:
                book.availability = False
                print(f"Book {title} has been borrowed. ")
            else:
                print("Book is not available.")
        else:
            print(f"Book '{title}' does not exist.")


    def return_book(self):
        title = input("Enter book to return: ")
        if title in books:
            self.availability=True
            print(f"Book {title} has been returned.")
        else:
            print(f"Book '{title}' does not exist.")

    def search_title(self):
        title = input("Enter title to search: ")
        if title in books:
            print(Book(title))

    def display_books(self):
        print(f"Books: {books}")


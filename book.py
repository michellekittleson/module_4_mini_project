books = []

class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability
   
    def add_book(title, author, genre, publication_date): 

        books.append(Book({'title': title, 'author': author, 'genre': genre, 'publication date': publication_date}))
        print(f"Book '{title}' has been added!")
 
    def borrow_book():
        title = input("Enter book to borrow: ").capitalize()
        book__found = None

        for book in books:
            if book.title == title:
                book_found = book
                break

            if book.availability == True:
                book.availability = False
                print(f"Book {title} has been borrowed. ")
            else:
                print("Book is not available.")
        else:
            print(f"Book '{title}' does not exist.")


    def return_book():
        title = input("Enter book to return: ")
        if title in books:
            books[title].availability=True
            print(f"Book {title} has been returned.")
        else:
            print(f"Book '{title}' does not exist.")

    def search_title():
        title = input("Enter title to search: ")
        if title in books:
            print(Book(title))

    def display_books():
        for book in books:
            print("Library Books:")
            print(f"Title: {books.title}")

default_book = Book("The Alchemist", "Paulo Coelho", "Fiction", 1988)
books.append(default_book)

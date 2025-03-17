from book import Book
from library import Library
from author import Author


def main():

    my_library = Library("The Library")

    # Add defaults
    # my_library.add_author("Paulo Coelho", "Paulo Coelho is a Brazilian author who has published many books.")
    # my_library.add_user("Alice", "1234")
    # my_library.add_user("Bob", "5678")
    # my_library.add_book("The Alchemist", "Paulo Coelho", "Fiction", 1988)


    while True:
        print("Welcome to the Library Management System!")
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")

        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
                choice = input("Enter your choice: ")
                try:
                    # Works!
                    if choice == '1':
                        title = input("Enter title: ")
                        author = input("Enter author: ")
                        genre = input("Enter genre: ")
                        publication_date = input("Enter publication date: ")
                        my_library.add_book(title, author, genre, publication_date)
                        print(f"Book '{title}' has been added!")
                        
                    # Even though the book is displaying properly after being added, it says "Book is either not in the library or is already checked out."
                    elif choice == '2':
                        title = input("Enter book to borrow: ").capitalize()
                        current_user = my_library.get_user(input("Enter user's name: "))
                        if current_user and my_library.borrow_book(title, current_user):
                            print(f"Book {title} has been borrowed.")
                        else:
                            print("Book is either not in the library or is already checked out.")
                    # "Book return failed" Could be because borrow book function is not working properly.
                    elif choice == '3':
                        title = input("Enter book to return: ").capitalize()
                        current_user = my_library.get_user(input("Enter user's name: "))
                        if current_user and my_library.return_book(title, current_user):
                            print(f"'{title}' has been returned.")
                        else:
                            print("Book return failed.")
                    # Works!
                    elif choice == '4':
                        title = input("Enter title to search: ")
                        if my_library.search_title(title):
                            print(f"Book '{title}' found.")
                        else:
                            print(f"Book '{title}' not found in the library.")
                    # Works!
                    elif choice == '5':
                        library_books = my_library.get_books()
                        for book in library_books:
                            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Date: {book.publication_date}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '2':
                print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
                choice = input("Enter your choice: ")
                try:
                    # Appears to work
                    if choice == '1':
                        name = input("Enter user name: ")
                        library_id = input("Enter library id: ") 
                        my_library.add_user(name, library_id)
                    # An error occurred: 'User' object has no attribute 'name'
                    elif choice == '2':
                        name = input("Enter user name: ")
                        user = my_library.get_user(name) # Retrieve user object
                        if user:
                            print(user.name)
                        else:
                            print("User not found.")
                    # An error occurred: 'User' object is not iterable
                    elif choice == '3':
                        all_users = my_library.get_users()
                        for user in all_users:
                            print(f"User name: {user.name}, Library ID: {user.library_id}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '3':
                print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
                choice = input("Enter your choice: ")
                try:
                    # Appears to work
                    if choice == '1':
                        name = input("Enter author name: ")
                        biography = input("Enter biography: ")
                        new_author = Author(name, biography)
                        my_library.add_author(new_author)
                        print(f"Author {name} has been added!")
                    # An error occurred: cannot access local variable 'author' where it is not associated with a value
                    elif choice == '2':
                        new_author.view_author_details()
                        print(f"Name: {author.name}, Biography: {author.biography}")
                    # An error occurred: 'NoneType' object is not iterable
                    elif choice == '3':
                        all_authors = my_library.display_authors()
                        for author in all_authors:
                            print(f"Name: {author.name}, Biography: {author.biography}")
                
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '4':
                print("Quitting system.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
from book import Book, Library
from author import Author


def main():

    my_library = Library("The Library")


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
                        
                    # An error occurred" 'Library' object has no attribute 'users'
                    elif choice == '2':
                        title = input("Enter book to borrow: ").capitalize()
                        current_user = my_library.get_user(input("Enter user's name: "))
                        if current_user and my_library.borrow_book(title, current_user):
                            print(f"Book {title} has been borrowed.")
                        else:
                            print("Book is either not in the library or is already checked out.")
                    # An error occurred: 'Library' object has no attribute 'users'
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
                    # An error occurred: 'Library' object has no attribute 'users'
                    if choice == '1':
                        name = input("Enter user name: ")
                        library_id = input("Enter library id: ") 
                        my_library.add_user(name, library_id)
                    # An error occurred: 'Library' object has no attribute 'users'
                    elif choice == '2':
                        name = input("Enter user name: ")
                        user = my_library.get_user(name) # Retrieve user object
                        if user:
                            print(user.name)
                        else:
                            print("User not found.")
                    # An error occurred: 'Library' object has no attribute '_Library__users'
                    elif choice == '3':
                        print(my_library.get_users())
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == '3':
                print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
                choice = input("Enter your choice: ")
                try:
                    # An error occurred: Library.add_author() missing 1 required positional argument: 'biography'
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
                    # Still need to make
                    elif choice == '3':
                        pass
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '4':
                print("Quitting system.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
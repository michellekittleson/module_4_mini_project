from book import Book, Library
from user import User
from author import Author

def main():


    while True:
        print("Welcome to the Library Management System!")
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")

        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
                choice = input("Enter your choice: ")
                try:
                    if choice == '1':
                        title = input("Enter title: ")
                        author = input("Enter author: ")
                        genre = input("Enter genre: ")
                        publication_date = input("Enter publication date: ")
                        Library.add_book(title, author, genre, publication_date)
                        print(f"Book '{title}' has been added!")
                        
                    elif choice == '2':
                        title = input("Enter book to borrow: ").capitalize()
                        if Library.borrow_book():
                            print(f"Book {title} has been borrowed. ")
                        else:
                            print("Book is not available.")

                    elif choice == '3':
                        Library.return_book()
                        print(f"'{title}' has been returned.")
                    elif choice == '4':
                        title = input("Enter title to search: ")
                        if Library.search_title():
                            print(f"Book '{title}' found.")
                        else:
                            print(f"Book '{title}' not found in the library.")
                    elif choice == '5':
                        library_books = Library.get_books()
                        for book in library_books:
                            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Date: {book.publication_date}")
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '2':
                print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
                choice == input("Enter your choice: ")
                try:
                    if choice == '1':
                        name = input("Enter name: ")
                        library_id = input("Enter library id: ")
                        User.add_user()
                    elif choice == '2':
                        name = input("Enter name: ")
                        print(User.name)
                    elif choice == '3':
                        User.display_users()
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '3':
                print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
                choice = input("Enter your choice: ")
                try:
                    if choice == '1':
                        Author.add_author()
                        print(f"Author {name} has been added!")
                    elif choice == '2':
                        Author.view_author_details()
                        print(f"Name: {author.name}, Biography: {author.biography}")
                    elif choice == '3':
                        Author.display_authors()
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '4':
                print("Quitting system.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
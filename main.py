from book import Book
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
                        Book.add_book()
                    elif choice == '2':
                        Book.borrow_book()
                    elif choice == '3':
                        Book.return_book()
                    elif choice == '4':
                        Book.search_title()
                    elif choice == '5':
                        Book.display_books()
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '2':
                print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
                choice == input("Enter your choice: ")
                try:
                    if choice == '1':
                        User.add_user()
                    elif choice == '2':
                        User.User.view_user_details()
                    elif choice == '3':
                        User.display_users()
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif choice == '3':
                print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
                choice = input("Enter your choice: ")
                try:
                    if choice == '1':
                        Author.add_author
                    elif choice == '2':
                        Author.view_author_details()
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
users = []

class User:
    def __init__(self, name, library_id, borrowed_books):
        self.name = name 
        self.library_id = library_id 
        self.borrowed_books = borrowed_books 

    def add_user(self):
        name = input("Enter name: ")
        library_id = input("Enter library id: ")
        users.append(User(name))

    def view_user_details(self):
        name = input("Enter name: ")
        print(User(name))

    def display_users(self):
        print(f"Users: {users}")
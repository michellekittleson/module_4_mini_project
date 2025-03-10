users = []

class User:
    def __init__(self, name, library_id, borrowed_books):
        self.name = name 
        self.library_id = library_id 
        self.borrowed_books = borrowed_books 

    def add_user(self):
        users.append(User.name)


    def display_users(self):
        for user in users:
            print(user)
authors = []

class Author:
    def __init__(self, name, biography):
        self.name = name 
        self.biography = biography 

    def add_author(self):
        name = input("Enter author's name: ")
        biography = input("Enter author's biography: ")
        authors.append(f"Name: {name}, Biography: {biography}")
        print(f"Author {name} has been added!")

    def view_author_details(self):
        name = input("Enter author's name: ")
        print(Author(name))

    def display_authors():
        print(f"Authors: {authors}")


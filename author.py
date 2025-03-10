authors = []

class Author:
    def __init__(self, name, biography):
        self.name = name 
        self.biography = biography 

    def add_author(self):
        name = input("Enter author's name: ")
        biography = input("Enter author's biography: ")
        authors.append(f"Name: {name}, Biography: {biography}")
        

    def view_author_details(self):
        name = input("Enter author's name: ")
        for author in authors:
            if name == author.name:
                return author
        

    def display_authors():
        for author in authors:
            print(author)
       


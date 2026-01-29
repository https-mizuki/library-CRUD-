class Book:
    books = []
    def __init__(self,id,title,author,year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        Book.books.append(self)
    def __str__(self):
        return f"ID:{self.id} | {self.title} by {self.author}, published in {self.year}"
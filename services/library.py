from models.books import Book

class Library:
    def __init__(self):
        self.books = []
    #adding a book to the list
    def add_book(self, book, title):
        self.books.append(book)
        book.title = title
        print(f"📘 Book '{book.title}' added successfully!")
    #reading the list of books
    def list_books(self):
        if not self.books:
            print("📭 There's no books listed")
        else:
            for book in self.books:
                print(book)
    #seartching books by id
    def seartch_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None
    def update_book(self, id, title, author, year):
        book =  self.seartch_by_id(id)
        if book:
            book.title = title
            book.author = author
            book.year = year
            print("✏️ Book succesfuly updated!")
            return
        else:
            print("❌ The current book does not exist")
    #deleting a book
    def delete_book(self, id):
        book = self.seartch_by_id(id)
        if book:
            self.books.remove(book)
            print(f"🗑️ Book removed succesfuly")
        else:
            print("❌ Book couldn't been removed, because this book does not exist")
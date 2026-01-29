from services.library import Library
from models.books import Book 

library = Library()

while True:
    print("\n===== MENU BIBLIOTECA =====")
    print("1 - Add Book")
    print("2 - List Books")
    print("3 - Update Books")
    print("4 - Delete Book")
    print("0 - Out")

    opcao = input("Choose an option: ")

    if opcao == "1":
        id = int(input("Book's ID: "))
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))

        book = Book(id, title, author, year)
        library.add_book(book,title)

    elif opcao == "2":
        library.list_books()
    elif opcao == "3":
        id = int(input("Book's ID for update: "))
        title = input("New title : ")
        author = input("New author: ")
        year = int(input("New year: "))

        library.update_book(id, title, author, year)

    elif opcao == "4":
        id = int(input("ID's book to remove: "))
        library.delete_book(id)

    elif opcao == "0":
        print("👋 Shutting down the system...")
        break

    else:
        print("❌ Invalid Option! Try Again.")

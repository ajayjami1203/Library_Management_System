import json
import os

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            print("Book ID is already exists.")
        else:
            self.books[book_id] = {"Title": title, "Author": author, "Copies": copies}
            self.save_books()
            print("Book added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print("Book removed successfully.")
        else:
            print("Book is not found.")

    def search_book(self, search_term):
        found_books = [book for book in self.books.values() if search_term.lower() in book["Title"].lower()]
        if found_books:
            print("Books Found:")
            for book in found_books:
                print(f"Title: {book['Title']}, Author: {book['Author']}, Copies: {book['Copies']}")
        else:
            print("No books found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:")
            for book_id, details in self.books.items():
                print(f"ID: {book_id}, Title: {details['Title']}, Author: {details['Author']}, Copies: {details['Copies']}")


def main():
    library = Library()
    while True:
        print("\n Welcome to Library Management System")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. View All Books")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                copies = int(input("Enter Number of Copies: "))
                library.add_book(book_id, title, author, copies)
            elif choice == 2:
                book_id = input("Enter Book ID to Remove: ")
                library.remove_book(book_id)
            elif choice == 3:
                search_term = input("Enter Book Title to Search: ")
                library.search_book(search_term)
            elif choice == 4:
                library.display_books()
            elif choice == 5:
                print("Exiting system. Library data saved.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

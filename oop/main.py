# --- Task 0: Book Class ---
from book_class import Book

print("=== Testing Book Class ===")
book = Book("1984", "George Orwell", 1949)
print(book)
print(repr(book))
del book

# --- Task 1: Library System ---
from library_system import Book as BaseBook, EBook, PrintBook, Library

print("\n=== Testing Library System ===")
library = Library()
library.add_book(BaseBook("Pride and Prejudice", "Jane Austen"))
library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))
library.list_books()

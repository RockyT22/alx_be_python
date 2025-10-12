# === Task 0: Testing Book Class (Magic Methods) ===
from book_class import Book

def test_book_class():
    print("=== Testing Book Class ===")
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)

    print(repr(my_book))

    del my_book


# === Task 1: Testing Library System (Inheritance & Composition) ===
from library_system import Book as BaseBook, EBook, PrintBook, Library

def test_library_system():
    print("\n=== Testing Library System ===")
    my_library = Library()

    classic_book = BaseBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


if __name__ == "__main__":
    test_book_class()
    test_library_system()

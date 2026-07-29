# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:20:18 2026

@author: mmerc
"""

class Book:
    
    def __init__(self, 
                 title: str,
                 author: str,
                 pages: int,
                 checked_out: bool = False
                 ):
        self.title = title
        self.author = author
        self.pages = pages
        self.checked_out = checked_out
        
    
    def check_out(self) -> None:
        self.checked_out = True
    
    
    def return_book(self) -> None:
        self.checked_out = False
    
    
    def reading_time(self, time_per_page: float) -> float:
        return self.pages * time_per_page
    
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
    
    def __repr__(self) -> str:      # used for representing objects in lists
        return str(self)

    
class Library:
    
    def __init__(self, books: list[Book] | None = None):
        # IMP SYNTAX: USE THIS FOR MUTABLE DEFAULTS
        if books is None:
            books = []
        
        self.books = books
    
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
        
    
    def remove_book(self, book: Book) -> Book:
        return self.books.remove(book)
    
    
    def find_book(self, title: str) -> Book:
        for b in self.books:
            if b.title == title:
                return b
        
        return None
        
    
    def available_books(self) -> list:
        return [
            b
            for b in self.books
            if not b.checked_out       # Note the syntax used here
        ]
    
    
    def total_pages(self) -> int:
        return sum(
            b.pages
            for b in self.books
        )
    
    
    def average_pages(self) -> int:
        return round(
            self.total_pages() / len(self.books)
        )
    
    def __str__(self) -> str:
        if not self.books:
            return "Library is empty."
    
        return "\n".join(str(book) for book in self.books)


def main() -> None:
    library = Library()
    
    library.add_book(Book("1984", "George Orwell", 173))
    library.add_book(Book("Animal Farm", "George Orwell", 231))
    library.add_book(Book("Boat", "Man", 24))
    
    print(library)
    
    book = library.find_book("1984")
    
    book.check_out()
    
    print(library.available_books())


if __name__ == "__main__":
    main()
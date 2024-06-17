from library.library import Library
from library.book import Book  
import pytest

class TestFonctionnel:

    @pytest.fixture()
    def list_book(self):
        librairy= Library()
        books=[
            Book(title="Cours Python", author="Imen"),
            Book(title="Cours Java", author="Jhon"),
            Book(title="Cours PHP", author="Eric")
        ]
        for elt in books:
            librairy.add_book(elt)
        return librairy
    
    def test_find_book_by_title_found(self, list_book):
        found_book = list_book.find_book_by_title("Cours Python")
        assert found_book.title == "Cours Python"
    
    def test_find_book_by_title_notfound(self, list_book):
        found_book = list_book.find_book_by_title("Cours")
        assert found_book is None
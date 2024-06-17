from library.library import Library
from library.book import Book  
import pytest

class TestLibrary:  # Utilisation de la convention de nommage correcte pour les classes de test
    @pytest.fixture()
    def list_fix(self, book_fix):
        return [book_fix]

    @pytest.fixture()
    def book_fix(self):
        return Book(title="Cours Python", author="Imen")

    def test_add_book(self, list_fix, book_fix):
        library = Library()
        library.add_book(book_fix)  
        assert library.books == list_fix

    def test_list_books(self,book_fix):
        library= Library()
        library.add_book(book_fix)
        assert  library.list_books() == ["Cours Python by Imen"]
    
    def test_remove_book(self, book_fix):
        library = Library()
        library.add_book(book_fix)
        library.remove_book(book_fix)
        assert library.books == []

    def test_remove_book_not_found(self, book_fix):
        library = Library()
        with pytest.raises(ValueError):
            library.remove_book(book_fix)
    




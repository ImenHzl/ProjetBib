import pytest
from library.book import Book  # Chemin d'importation correct

class TestBook:
    @pytest.fixture()
    def book_fix(self):
        book = Book(title="Cours Python", author="Imen")
        return book

    def test_init(self, book_fix):
        assert book_fix.title == "Cours Python"
        assert book_fix.author == "Imen"

    def test_str(self, book_fix):
        assert str(book_fix) == "Cours Python by Imen"

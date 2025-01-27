import pytest
from main import BooksCollector


@pytest.fixture
def prepare_books_collector():
    collector = BooksCollector()
    collector.add_new_book('Туман')
    collector.add_new_book('Ревизор')
    collector.add_new_book('Оно')
    collector.set_book_genre('Туман', 'Ужасы')
    collector.set_book_genre('Ревизор', 'Комедии')
    collector.set_book_genre('Оно', 'Ужасы')
    return collector

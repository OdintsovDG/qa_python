from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_made_dictionary_empty_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_made_list_empty_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_list_of_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_list_of_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_set_book_genre_for_add_new_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Туман')
        collector.set_book_genre('Туман', 'Ужасы')
        assert collector.books_genre['Туман'] == 'Ужасы'

    @pytest.mark.parametrize('book_name, book_genre', [['Туман', 'Ужасы'], ['Ревизор', 'Комедии']])
    def test_get_book_genre_two_book_with_genre_true(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_two_horror_books_in_list(self, prepare_books_collector):
        collector = prepare_books_collector
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_get_dictionary_true(self):
        collector = BooksCollector()
        collector.add_new_book('Туман')
        collector.set_book_genre('Туман', 'Ужасы')
        assert collector.get_books_genre() == {'Туман': 'Ужасы'}

    def test_get_books_for_children_comedy_book_in_list_true(self, prepare_books_collector):
        collector = prepare_books_collector
        assert collector.get_books_for_children() == ['Ревизор']

    def test_add_book_in_favorites_add_two_book(self, prepare_favorites_books_collector):
        collector = prepare_favorites_books_collector
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_del_one_book(self, prepare_favorites_books_collector):
        collector = prepare_favorites_books_collector
        collector.delete_book_from_favorites('Туман')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_get_list_true(self):
        collector = BooksCollector()
        collector.add_new_book('Туман')
        collector.add_book_in_favorites('Туман')
        assert collector.get_list_of_favorites_books() == ['Туман']

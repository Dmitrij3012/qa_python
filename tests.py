import pytest


class TestBooksCollector:

    @pytest.mark.parametrize(
        'name',
        [
            'Г',
            'Го',
            'Гордость и предубеждение',
            'Что делать, если ваш кот хочет вас убить'
        ]
    )
    def test_add_new_book_from_1_to_40_symbols_positive(self, collector, name):
        collector.add_new_book(name)

        assert name in collector.books_genre

    @pytest.mark.parametrize(
        'name',
        [
            'Что делать, если ваш кот хочет вас убитьь',
            'Что делать, если ваш кот хочет вас убитькот хочет вас убить'
        ]
    )
    def test_add_new_book_over_40_symbols_negative(self, collector, name):
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_add_new_book_re_adding_negative(self, collector):
        name = 'Гордость и предубеждение'

        collector.add_new_book(name)
        collector.add_new_book(name)
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_with_empty_line_negative(self, collector):
        name = ''

        collector.add_new_book(name)

        assert name not in collector.books_genre

    def test_set_book_genre_positive(self, collector):
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[1])

        assert collector.get_book_genre(name) == 'Ужасы'

    def test_get_book_genre_without_genre_positive(self, collector):
        name = 'Война и мир'

        collector.add_new_book(name)

        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_with_genre_positive(self, collector):
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[1])

        assert collector.get_book_genre(name) == 'Ужасы'

    @pytest.mark.parametrize(
        'name,genre,expected_result',
        [
            ['Гордость и предубеждение и зомби', 1, 'Гордость и предубеждение и зомби'],
            ['Человек-амфибия', 0, 'Человек-амфибия'],
            ['Котёнок по имени Гав', 3, 'Котёнок по имени Гав']
        ]
    )
    def test_get_books_with_specific_genre_positive(self, collector, name, genre, expected_result):
        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[genre])

        assert collector.get_books_with_specific_genre(collector.genre[genre]) == [expected_result]

    def test_get_books_genre_without_genre_positive(self, collector):
        name = 'Гордость и предубеждение и зомби'
        expected_dict = {'Гордость и предубеждение и зомби': ''}

        collector.add_new_book(name)

        assert collector.get_books_genre() == expected_dict

    @pytest.mark.parametrize(
        'name,genre,expected_dict',
        [
            ['Что делать, если ваш кот хочет вас убить', 1, {'Что делать, если ваш кот хочет вас убить': 'Ужасы'}],
            ['Человек-амфибия', 0, {'Человек-амфибия': 'Фантастика'}],
            ['Котёнок по имени Гав', 3, {'Котёнок по имени Гав': 'Мультфильмы'}]
        ]
    )
    def test_get_books_genre_positive(self, collector, name, genre, expected_dict):
        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[genre])

        assert collector.get_books_genre() == expected_dict

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Человек-амфибия', 0],
            ['Котёнок по имени Гав', 3]
        ]
    )
    def test_get_books_for_children_positive(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[genre])

        assert name in collector.get_books_for_children()

    def test_get_books_for_children_negative(self, collector):
        name = 'Гордость и предубеждение и зомби'

        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[1])

        assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_positive(self, collector):
        name = 'Человек-амфибия'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_non_existent_book_negative(self, collector):
        name = 'Человек-амфибия'

        collector.add_book_in_favorites(name)

        assert name not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_re_adding_negative(self, collector):
        name = 'Человек-амфибия'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_positive(self, collector):
        name = 'Котёнок по имени Гав'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.favorites

    def test_delete_book_from_favorites_negative(self, collector):
        name = 'Котёнок по имени Гав'

        collector.add_new_book(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.favorites

    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение и зомби',
            'Человек-амфибия',
            'Котёнок по имени Гав',
        ]
    )
    def test_get_list_of_favorites_books_positive(self,  collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

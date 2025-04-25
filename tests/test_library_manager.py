# tests/test_library_manager.py
"""
Модуль содержит тесты для проверки функциональности различных
компонентов библиотеки, включая классы и функции.
"""

import unittest
from library_manager import Library, generate_report, validate_book_data

class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        """Создает новый экземпляр библиотеки перед каждым тестом."""
        self.library = Library()

    def test_add_book(self):
        """Тестирует добавление книги в библиотеку."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        self.assertEqual(len(self.library.view_books()), 1)

    def test_remove_book(self):
        """Тестирует удаление книги из библиотеки."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        self.library.remove_book("Book Title")
        self.assertEqual(len(self.library.view_books()), 0)

    def test_remove_non_existent_book(self):
        """Тестирует удаление книги, которая не существует в библиотеке."""
        with self.assertRaises(ValueError):
            self.library.remove_book("Non-existent Title")

    def test_find_book(self):
        """Тестирует поиск книги по названию."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        result = self.library.find_book(title="Book Title")
        self.assertEqual(len(result), 1)

    def test_find_book_by_author(self):
        """Тестирует поиск книги по автору."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        result = self.library.find_book(author="Author Name")
        self.assertEqual(len(result), 1)

    def test_find_book_by_genre(self):
        """Тестирует поиск книги по жанру."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        result = self.library.find_book(genre="Fiction")
        self.assertEqual(len(result), 1)

    def test_find_non_existent_book(self):
        """Тестирует поиск несуществующей книги."""
        result = self.library.find_book(title="Non-existent Title")
        self.assertEqual(len(result), 0)

    def test_generate_report(self):
        """Тестирует генерацию отчета для книг в библиотеке."""
        self.library.add_book("Book Title", "Author Name", "Fiction")
        report = generate_report(self.library)
        self.assertIn("Title: Book Title", report)

    def test_validate_book_data(self):
        """Тестирует валидацию корректных данных книги."""
        valid_data = {'title': 'Valid Title', 'author': 'Valid Author', 'genre': 'Fiction'}
        self.assertTrue(validate_book_data(valid_data))

    def test_invalid_book_data_missing_field(self):
        """Тестирует валидацию некорректных данных книги с отсутствующим полем."""
        invalid_data = {'title': 'Invalid Title', 'author': 'Valid Author'}
        self.assertFalse(validate_book_data(invalid_data))

        if __name__ == '__main__':
            unittest.main()
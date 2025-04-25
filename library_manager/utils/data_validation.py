# library_manager/utils/data_validation.py
"""
Модуль содержит функции для валидации данных книг.
Метод:
- def validate_book_data(data): Проверяет корректность данных книги.
  Args:
data (dict): Словарь с данными книги.
Возвращает bool: True, если данные корректные, иначе False.
"""

def validate_book_data(data):
    """Проверяет корректность данных книги."""
    required_keys = ['title', 'author', 'genre']
    return all(key in data for key in required_keys)
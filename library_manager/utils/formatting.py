# library_manager/utils/formatting.py
"""
Модуль содержит функции для форматирования данных.
Метод:
- def format_book_data(data): Форматирует данные книги для вывода в отчет.
  Args:
data (dict): Словарь с данными книги.
Возвращает str: Строка с отформатированными данными книги.
"""

def format_book_data(data):
    """Форматирует данные книги для вывода в отчет."""
    return f"Title: {data['title']}, Author: {data['author']}, Genre: {data['genre']}"
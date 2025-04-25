# library_manager/report.py
"""
Модуль содержит функции для генерации отчетов о книгах в библиотеке.
Метод:
- def generate_report(library): Генерирует отчет в формате строки.
  Args:
library (Library): Экземпляр класса Library.  
"""

def generate_report(library):
    """Генерирует отчет о всех книгах в библиотеке в формате строки."""
    report_lines = []
    for book in library.view_books():
        report_lines.append(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    return "\n".join(report_lines)
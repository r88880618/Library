# library_manager/catalog.py
"""
Модуль catalog.py содержит класс Library, который управляет книгами в библиотеке.
Класс включает методы:
- def __init__(self): Создает экземпляр библиотеки с пустым списком книг. 

- def add_book(self, title, author, genre): Добавляет книгу в библиотеку.
  Args:
title (str): Название книги.
author (str): Автор книги.
genre (str): Жанр книги.

- def remove_book(self, title): Удаляет книгу по названию.
  Args:
title (str): Название книги для удаления.
В метод добавляем проверку if ... raise - логику выбрасывания исключения в случае, 
если книга с указанным названием не найдена.

- def find_book(self, title=None, author=None, genre=None):Ищет книги
по названию, автору и жанру.
  Args:
title (str, optional): Название книги для поиска.
author (str, optional): Автор книги для поиска.
genre (str, optional): Жанр книги для поиска.

- def view_books(self): Возвращает список всех книг в библиотеке.
"""

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, title, author, genre):
        book = {'title': title, 'author': author, 'genre': genre}
        self.books.append(book)

    def remove_book(self, title):
        # Проверяем, существует ли книга, прежде чем пытаться удалить ее
        if not any(book['title'] == title for book in self.books):
            raise ValueError(f"Книга с названием '{title}' не найдена.")
        self.books = [book for book in self.books if book['title'] != title]

    def find_book(self, title=None, author=None, genre=None):
        results = self.books
        if title:
            results = [book for book in results if book['title'] == title]
        if author:
            results = [book for book in results if book['author'] == author]
        if genre:
            results = [book for book in results if book['genre'] == genre]
        return results

    def view_books(self):
        return self.books
# library_manager/__init__.py
"""
Инициализатор пакета library_manager. Этот файл управляет импортом
основных компонентов пакета.
"""

from .catalog import Library
from .report import generate_report
from .utils.data_validation import validate_book_data 

__all__ = ['Library', 'generate_report', 'validate_book_data']
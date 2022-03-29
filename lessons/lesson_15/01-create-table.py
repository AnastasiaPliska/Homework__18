"""
Создание таблицы

Таблица - books
Столбцы - name, author, description
"""

import sqlite3

with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE books (
            name,
            author,
            description
        )
    """

    cursor.execute(query)
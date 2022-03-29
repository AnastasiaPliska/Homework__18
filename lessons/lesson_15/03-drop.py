"""
Создание таблицы

Таблица - books
Столбцы - id, name, author, description, genre, publication_date, pages_count, price

ADD, RENAME, DROP
"""

import sqlite3

with sqlite3.connect("books_db_2.sqlite") as connection:
    cursor = connection.cursor()

    query = """
          DROP TABLE books_2;      
        """

    cursor.execute(query)

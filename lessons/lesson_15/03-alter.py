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
        ALTER TABLE books_3 RENAME text TO description
    """

    # query = """
    #         ALTER TABLE books_3
    #         ADD publication_country varchar(100)
    #     """

    # query = """
    #         ALTER TABLE books_3 DROP COLUMN publication_country - удаление коллонки
    #     """

    cursor.execute(query)

"""
Удаление строк из таблицы
"""

import sqlite3

with sqlite3.connect("books_db_2.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        DELETE FROM books_3
        WHERE price < 130
    """

    cursor.execute(query)

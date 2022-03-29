"""
Создание базы данных SQLite3 - books_db
"""

import sqlite3

with sqlite3.connect("books_db.sqlite") as connection:
    cursor = connection.cursor()

    cursor.execute()
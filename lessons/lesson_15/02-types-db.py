"""
Создание таблицы

Таблица - books
Столбцы - name, author, description, genre, publication_date, pages_count, price

Типы - bit, int, decimal, float, date, time, datetime, varchar
"""

import sqlite3

with sqlite3.connect("books_db_2.sqlite") as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE books_2 (
            name varchar(40),
            author varchar(80),
            description varchar(255),
            genre varchar(20), 
            publication_date date, 
            pages_count integer, 
            price decimal
        )
    """

    cursor.execute(query)


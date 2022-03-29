"""
Добавление новых значений (одиночное, множественное)
"""

import sqlite3

with sqlite3.connect("books_db_2.sqlite") as connection:
    cursor = connection.cursor()

    # Одиночное
    # query = """
    #       INSERT INTO books_3 (name, pages_count) VALUES ('New book', 36)
    #     """

    # Множественное
    query = """
              INSERT INTO books_3 (name, pages_count) 
              VALUES ('New book 2', 53), ('Second book', 49)   
            """

    cursor.execute(query)

"""
Редактирование строк в таблице (полное, условное)

ПримерыЖ
- добавление описания книги
- переименовать жанр
- увеличить стоимость на 10%
"""

import sqlite3

with sqlite3.connect("books_db_2.sqlite") as connection:
    cursor = connection.cursor()

    # query = """
    #     UPDATE books_3
    #     SET genre = 'None'
    #     WHERE id=1
    # """

    # query = """
    #         UPDATE books_3
    #         SET description = 'Some description content'
    #         WHERE id=3
    #     """

    # query = """
    #             UPDATE books_3
    #             SET price = 100
    #             WHERE price IS NULL
    #         """

    query = """
                UPDATE books_3
                SET price = price + 30
                WHERE id IN (1,2)               
            """

    cursor.execute(query)

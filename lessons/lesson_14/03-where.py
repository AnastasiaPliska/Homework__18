"""
Фильтрация данных
Условия - совпадение, диапазоны, вхождения, пустые значения
Комбинации - логические операторы
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()

    # query = """
    #         SELECT *  - все столбцы
    #         FROM netflix
    #         WHERE director = 'Cristina Jacob'
    #         lIMIT 10
    #         OFFSET 10
    # """

    # query = """
    #         SELECT director, duration  - поиск по указанным столбцам
    #         FROM netflix
    #         WHERE director = 'Cristina Jacob'
    #         AND duration > 110
    # """

    # query = """
    #         SELECT *
    #         FROM netflix
    #         WHERE country = 'Russia' OR country = 'Romania' - так долго писать проще НИЖЕ пример
    # """

    # query = """
    #         SELECT title, country
    #         FROM netflix
    #         WHERE country IN ('Russia', 'Romania') -  а вот так лучше
    # """

    # query = """
    #         SELECT title, country
    #         FROM netflix
    #         WHERE country LIKE 'R%'  - (R% - начинается с буквы R
    #                                     %R - Заканчивается на букву R
    #                                     %R% - содержит в середине букву R)
    # """

    # query = """
    #         SELECT title, country
    #         FROM netflix
    #         WHERE netflix.cast LIKE '%Maria%'
    #         или
    #         WHERE "cast" LIKE '%Maria%'
    #         т.к. cast зарезервированное слово,
    #         то можно использовать двойные кавычки (этот вариант используют чаще)
    #         или указывать впереди через точку файл,
    #         пример выше
    # """

    # query = """
    #         SELECT "cast"
    #         FROM netflix
    #         WHERE release_year > 2000
    # """

    # query = """
    #         SELECT release_year, title
    #         FROM netflix
    #         WHERE release_year <1950
    # """

    # query = """
    #         SELECT "cast"
    #         FROM netflix
    #         WHERE release_year < 1950 AND release_year > 1945  - так долго писать проще НИЖЕ пример
    # """

    # query = """
    #         SELECT "cast"
    #         FROM netflix
    #         WHERE release_year BETWEEN 1945 AND 1950 - а вот так лучше
    #                         BETWEEN работает как больше или равно и меньше или равно (учитывает границы промежутка)
    # """

    # query = """
    #         SELECT release_year, title, director
    #         FROM netflix
    #         WHERE release_year BETWEEN 1945 AND 1950
    #         AND director != ''  - режисер не равен пустой строке
    # """

    query = """
            SELECT release_year, title, director
            FROM netflix
            WHERE director != ''  - режисер не равен пустой строке, но строка есть, просто она пустая                         
            или 
            WHERE direct IS NOT NULL  - а вот такая запись говорит, что совсем пусто, т.е. там во всем столбце пусто вообще ничего не заполнено 
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
"""
Сортировка данных (обычная и множественная)
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT title, release_year, duration
            FROM netflix
            ORDER BY release_year DESC, duration DESC 
            LIMIT 10
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
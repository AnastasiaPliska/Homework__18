"""
Группировка данных
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT type, country
            FROM netflix
            WHERE country != ''
            GROUP BY type, country
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
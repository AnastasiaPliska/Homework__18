"""
Подключение к SQLite 3
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM netflix")

    for row in cursor.fetchall():
        print(row)
        # fetchall - говорит сколько результата вывести (fetchone - один, fetchall - всё или fetchmany - несколько);

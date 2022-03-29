"""
Подключение к SQLite 3
"""

import sqlite3

with sqlite3.connect("здесь указать файл с базой данных") as connection:
    cursor = connection.cursor()
    cursor.execute("ЗДЕСЬ БУДУТ НАШИ КОМАНДЫ")
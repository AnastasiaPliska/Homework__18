"""
HAVING()
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()

    query = """
            SELECT country, SUM(duration) as total_duration
            FROM netflix 
            WHERE type = 'TV Show' 
            AND country != ''
            GROUP BY country
            HAVING total_duration BETWEEN 2 AND 10
            ORDER BY total_duration
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
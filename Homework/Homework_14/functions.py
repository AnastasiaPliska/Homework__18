import json
import sqlite3
from collections import Counter


def db_connect(db, query):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    con.close()
    return result


def get_rating(rating):
    response = []
    if len(rating)>1:
        str_rating = "','".join(rating)
    else:
        str_rating = "".join(rating)
    query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating in ('{str_rating}')
            LIMIT 100
    """
    result = db_connect('netflix.db', query)
    for line in result:
        line_dict = {
            "title": line[0],
            "rating": line[1],
            "description": line[2]
        }
        response.append(line_dict)
    return response


def get_cast(actor1, actor2):
    query = f"""
                SELECT "cast"
                FROM netflix
                WHERE "cast" LIKE '%{actor1}%' 
                AND "cast" LIKE '%{actor2}%'
        """
    result = db_connect('netflix.db', query)
    result_list = []
    for line in result:
        line_list = line[0].split(',')
        result_list += line_list
    counter = Counter(result_list)

    actors_list = []
    for key, value in counter.items():
        if value > 2 and key.strip() not in [actor1, actor2]:
            actors_list.append(key)
    return actors_list


def get_film_list(type, release_year, genre):
    query = f"""
                SELECT title, description
                FROM netflix
                WHERE type = '{type}' 
                AND release_year = '{release_year}'
                AND "listed_in" LIKE '%{genre}%'
        """
    result = db_connect('netflix.db', query)
    response = []
    for line in result:
        line_dict = {
            "title": line[0],
            "description": line[1],
        }
        response.append(line_dict)
    return json.dumps(response)


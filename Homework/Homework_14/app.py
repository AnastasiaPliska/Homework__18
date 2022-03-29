from flask import Flask, request, jsonify
from functions import db_connect, get_rating

app = Flask(__name__)

@app.route("/movie/title", methods=['GET'])
def search_title():
    if request.method == 'GET':
        response = {}
        title = request.args.get('title')
        if title:
            query = f"""
            SELECT title, country, listed_in, release_year, description
            FROM netflix
            WHERE title = '{title}'
            ORDER BY release_year DESC 
            LIMIT 1
            """
            result = db_connect('netflix.db', query)
            if len(result):
                response = {
                    "title" : result[0][0],
                    "country": result[0][1],
                    "listed_in": result[0][2],
                    "release_year": result[0][3],
                    "description": result[0][4],
                }
        return jsonify(response)


@app.route("/movie/year/", methods=['GET'])
def search_year():
    if request.method == 'GET':
        response = []
        first_year = request.args.get('first_year')
        last_year = request.args.get('last_year')
        if first_year and last_year:
            query = f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {first_year} AND {last_year}
                    LIMIT 100 
            """
            result = db_connect('netflix.db', query)
            for line in result:
                line_dict = {
                    "title": line[0],
                    "release_year": line[1]
                }
                response.append(line_dict)
        return jsonify(response)


@app.route("/rating/children")
def films_children():
    response = get_rating(['G'])
    return jsonify(response)


@app.route("/rating/family")
def films_family():
    response = get_rating(['G', 'PG', 'PG-13'])
    return jsonify(response)


@app.route("/rating/adult")
def films_adult():
    response = get_rating(['R', 'NC-17'])
    return jsonify(response)


@app.route("/genre/<genre>/")
def search_genre(genre):
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE "listed_in" LIKE '%{genre}%'
            AND type = 'Movie'
            ORDER BY release_year DESC
            LIMIT 10
            """
    result = db_connect('netflix.db', query)
    response = []
    for line in result:
        line_dict = {
            "title": line[0],
            "description": line[1],
        }
        response.append(line_dict)
    return jsonify(response)


app.run(debug=True)
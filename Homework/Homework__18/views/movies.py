from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)

        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if not movie:
            return "", 404
        return movie_schema.dump(movie), 200


    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update(req_json)

        return "", 204


    def patch(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)

        return "", 204


    def delete(self, mid: int, movie_service=None):
        movie_service.delete(mid)

        return "", 204


from dao.movie import MovieDAO

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        movie = self.dao.get_one(mid)
        if not movie:
            return "", 404
        return movie

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_all_by_director(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_all_by_genre(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_all_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, mov_data):
        return self.dao.create(mov_data)

    def update(self, mov_data):
        mid = mov_data.get("id")
        movie = self.get_one(mid)

        movie.title = mov_data.get("title")
        movie.description = mov_data.get("description")
        movie.trailer = mov_data.get("trailer")
        movie.year = mov_data.get("year")
        movie.rating = mov_data.get("rating")
        movie.genre_id = mov_data.get("genre_id")
        movie.director_id = mov_data.get("director_id")

        self.dao.update(movie)

    def update_partial(self, mov_data):
        mid = mov_data.get("id")
        movie = self.get_one(mid)

        if "title" in mov_data:
            movie.title = mov_data.get("title")
        if "description" in mov_data:
            movie.description = mov_data.get("description")
        if "trailer" in mov_data:
            movie.trailer = mov_data.get("trailer")
        if "year" in mov_data:
            movie.year = mov_data.get("year")
        if "rating" in mov_data:
            movie.rating = mov_data.get("rating")
        if "genre_id" in mov_data:
            movie.genre_id = mov_data.get("genre_id")
        if "director_id" in mov_data:
            movie.director_id = mov_data.get("director_id")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

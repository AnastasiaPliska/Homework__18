from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)


    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_by_director(self, m_dir):
        return self.session.query(Movie).filter(Movie.director_id == m_dir).all()

    def get_all_by_genre(self, m_genre):
        return self.session.query(Movie).filter(Movie.genre_id == m_genre).all()

    def get_all_by_year(self, m_year):
        return self.session.query(Movie).filter(Movie.year == m_year).all()


    def create(self, mov_data):
        movie = Movie(**mov_data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, mov_data):
        movie = self.get_one(mov_data.get("id"))
        movie.title = mov_data.get("title")
        movie.description = mov_data.get("description")
        movie.trailer = mov_data.get("trailer")
        movie.year = mov_data.get("year")
        movie.rating = mov_data.get("rating")
        movie.genre_id = mov_data.get("genre_id")
        movie.director_id = mov_data.get("director_id")

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

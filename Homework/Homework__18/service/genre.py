from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        genre = self.dao.get_one(gid)
        if not genre:
            return "", 404
        return genre

    def get_all(self):
        return self.dao.get_all()

from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        director = self.dao.get_one(did)
        if not director:
            return "", 404
        return director

    def get_all(self):
        return self.dao.get_all()

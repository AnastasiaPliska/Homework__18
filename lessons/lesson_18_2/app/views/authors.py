from flask import request
from flask_restx import Resource, Namespace

from lesson_18_2.app.container import author_service
from lesson_18_2.app.dao.model.author import AuthorSchema

author_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

@author_ns.route('/')    #    / + authors + /
class AuthorsView(Resource):
    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        author_service.create(req_json)

        return "", 201


@author_ns.route('/<int:aid>')
class AuthorView(Resource):
    def get(self, aid: int):  # Получение данных
        author = author_service.get_one(aid)
        return author_schema.dump(author), 200


    def put(self, aid): # Замена данных
        req_json = request.json
        req_json["id"] = aid

        author_service.update(req_json)

        return "", 204


    def patch(self, aid):  # Частичное обновление данных
        req_json = request.json
        req_json["id"] = aid
        author_service.update_partial(req_json)

        return "", 204


    def delete(self, aid: int):
        author_service.delete(aid)

        return "", 204

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

""" Создаем приложение Flask """
app = Flask(__name__)
""" Настраиваем работу с базой данных """
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
""" Создаем соединение с базой данных """
db = SQLAlchemy(app)

"""Описываем модель"""
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)

"""Готовим схему для сериализации и десериализации через маршмелоу"""
class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()

"""Готовим объект чтобы сериализовать и десериализовать в единственном экземпляре и множественных объектов (списков)"""
book_schema = BookSchema()
books_schema = BookSchema(many=True)

"""Создаем объект API"""
api = Api(app)
"""Регистрируем неймспейс для работы с книгами"""
book_ns = api.namespace('')

""" Создаем 2 книги в виде сущностей от класса модели"""
b1 = Book(id=1, name="Harry Potter", year=1992, author="Joan Rouling")
b2 = Book(id=2, name="Le Comte de Monte-Cristo", year=1854, author="Alexandre Dumas")

"""Создаем таблицы"""
db.create_all()


"""При помощи открытия сессии сохраняем книги в базу"""
with db.session.begin():
    db.session.add_all([b1, b2])


"""Как выглядят роуты с измененными и обновленными значениями"""
@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Book).all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Book(**req_json)
        with db.session.begin():
            db.session.add(new_book)
        return "", 201


@book_ns.route('/books/<int:bid>')
class BookView(Resource):
    def get(self, bid: int):  # Получение данных
        try:
            book = db.session.query(Book).filter(Book.id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404


    def put(self, bid): # Замена данных
        book = db.session.query(Book).get(bid)
        req_json = request.json

        book.name = req_json.get("name")
        book.year = req_json.get("year")
        book.author = req_json.get("author")

        db.session.add(book)
        db.session.commit()

        return "", 204


    def patch(self, bid):  # Частичное обновление данных
        book = db.session.query(Book).get(bid)
        req_json = request.json

        if "name" in req_json:
            book.name = req_json.get("name")
        if "year" in req_json:
            book.year = req_json.get("year")
        if "author" in req_json:
            book.author = req_json.get("author")

        db.session.add(book)
        db.session.commit()

        return "", 204


    def delete(self, bid: int):  
        book = db.session.query(Book).get(bid)

        db.session.delete(book)
        db.session.commit()

        return "", 204


if __name__ == '__main__':
    app.run(debug=False)


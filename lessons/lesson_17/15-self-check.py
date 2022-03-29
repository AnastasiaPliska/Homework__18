# Как сконфигурировать Flask-RESTX ?
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

# Как создать namespace?
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)
notes_ns = api.namespace('notes')

# Как сделать Class Based View с использованием REST X?
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)
book_ns = api.namespace('books')

# здесь регистрируем класс (CBV) (ресурс) по определенному пути (эндпоинту)
@book_ns.route('/')
# наследуем класс от класса Resource
class BooksView(Resource):
# пишем все нужные методы

# получение списка сущностей, мы отдаем список всех сущностей из БД
    def get(self):
        all_books = Book.query.all()
        return books_schema.dump(all_books), 200
# создание сущности, здесь мы получаем данные из запроса и создаем новую сущность в БД
    def post(self):
        req_json = request.json
        new_user = Book(**req_json)
        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@book_ns.route('/<int:uid>')
class BookView(Resource):
# получение конкретной сущности по идентификатору
    def get(self, uid: int):
        try:
            book = Book.query.get(uid)
            return book_schema.dump(book), 200
        except Exception as e:
            return "", 404

# обновление сущности по идентификатору
    def put(self, uid):
        book = Book.query.get(uid)
        req_json = request.json
        book.name = req_json.get("name")
        book.email = req_json.get("email")
        book.age = req_json.get("age")
        db.session.add(book)
        db.session.commit()
        return "", 204

# частичное обновление сущности, здесь мы получаем только часть полей и их обновляем у сущности
    def patch(self, uid):
        book = Book.query.get(uid)
        req_json = request.json
        if "name" in req_json:
            book.name = req_json.get("name")
        if "email" in req_json:
            book.email = req_json.get("email")
        if "age" in req_json:
            book.age = req_json.get("age")
        db.session.add(book)
        db.session.commit()
        return "", 204

# удаление сущности
    def delete(self, uid: int):
        user = Book.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return "", 204


""" 
Почему CBV лучше чем функции?

- Повышается читаемость кода
- Повышается тестируемость - все методы в одном классе
- Не надо дополнительных условий на проверку методов
"""

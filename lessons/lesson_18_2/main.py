from flask import Flask
from flask_restx import Api
from sqlalchemy.testing import db

from app.config import Config
from app.views.authors import author_ns
from app.views.books import book_ns
from lesson_18_2.app.dao.model.author import Author
from lesson_18_2.app.dao.model.book import Book


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(book_ns) # books
    api.add_namespace(author_ns) # authors

def load_data():
    b1 = Book(id=1, name="Harry Potter", year=1992)
    b2 = Book(id=2, name="Le Comte de Monte-Cristo", year=1854)

    a1 = Author(id=1, first_name="Joan", last_name="Rouling")
    a2 = Author(id=2, first_name="Alexandre", last_name="Dumas")

    db.create_all()


    with db.session.begin():
        db.session.add_all([a1, a2])
        db.session.add_all([b1, b2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    load_data()

    app.run()

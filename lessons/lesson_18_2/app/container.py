from lesson_18_2.app.dao.author import AuthorDAO
from lesson_18_2.app.dao.book import BookDAO
from lesson_18_2.app.database import db
from lesson_18_2.app.services.author import AuthorService
from lesson_18_2.app.services.book import BookService

author_dao = AuthorDAO(db.session)
author_service = AuthorService(author_dao)

book_dao = BookDAO(db.session)
book_service = BookService(book_dao)

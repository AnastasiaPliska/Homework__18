-- Настройка внешних ключей в таблицах
--
-- Таблицы - books, author, genres
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
    genre_id INTEGER FOREIGN KEY REFERENCES genres(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE book_author (
    book_id INTEGER FOREIGN KEY REFERENCES books(id),
    author_id INTEGER FOREIGN KEY REFERENCES author(id),
    PRIMARY KEY (book_id, author_id)
);
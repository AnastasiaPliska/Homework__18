-- Выборка связанных данных
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    genre_id INTEGER,
    FOREIGN KEY(genre_id) REFERENCES genres(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE book_author (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

INSERT INTO genres (name)
VALUES ('Horror'), ('Sci-Fi');

INSERT INTO author (name)
VALUES ('Author 1'), ('Author 2'), ('Author 3');

INSERT INTO books (name, genre_id)
VALUES ('Book 1', 1), ('Book 2', 2), ('Book 3', 3);

INSERT INTO book_author (book_id, author_id)
VALUES (1, 1), (2, 1), (2, 3);
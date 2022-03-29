-- Применение нормальных форм
--
-- 3НФ - выносим повторения в отдельные таблицы

CREATE TABLE duration_type
(
    id       integer PRIMARY KEY AUTOINCREMENT,
    name     varchar(100)
);

CREATE TABLE shows_duration
(
    id       integer PRIMARY KEY AUTOINCREMENT,
    type_id     integer,
    duration integer NOT NULL,
    FOREIGN KEY (type_id) REFERENCES duration_type(id)
);

CREATE TABLE show_type
(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar(100)
);

CREATE TABLE shows
(
    id integer PRIMARY KEY AUTOINCREMENT,
    type_id integer,
    title text,
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration_id integer,
--     duration int,
--     duration_type text,
    description text,
    FOREIGN KEY (duration_id) REFERENCES shows_duration(id),
    FOREIGN KEY (type_id) REFERENCES show_type(id)
);

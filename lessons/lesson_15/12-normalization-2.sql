-- Применение нормальных форм
--
-- 2НФ - выделяем связи между столбцами в отдельные таблицы

CREATE TABLE shows_duration
(
    id       integer PRIMARY KEY AUTOINCREMENT,
    type     varchar(100),
    duration integer NOT NULL
);

CREATE TABLE shows
(
    id integer PRIMARY KEY AUTOINCREMENT,
    type text,
    title text,
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration_id integer,
--     duration int,
--     duration_type text,
    description text,
    FOREIGN KEY (duration_id) REFERENCES shows_duration(id)
);

-- Применение нормальных форм
--
-- 1НФ - вносим массивы значений столбца в разные таблицы

CREATE TABLE netflix
(
    show_id text,
    type text,
    title text,
    director text,
    cast text,
    country text,
    date_added datetime,
    release_year int,
    rating text,
    duration int,
    duration_type text,
    listed_in text,
    description text
);

-- новый формат

CREATE TABLE directors
(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar (100) NOT NULL

);

CREATE TABLE actors
(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar (100) NOT NULL

);

CREATE TABLE categories
(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar (100) NOT NULL

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
    duration int,
    duration_type text,
    description text
);

CREATE TABLE show_director
(
    show_id integer,
    director_id integer,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (director_id) REFERENCES directors(id)
);

CREATE TABLE show_actors
(
    show_id integer,
    actor_id integer,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);

CREATE TABLE show_categories
(
    show_id integer,
    category_id integer,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

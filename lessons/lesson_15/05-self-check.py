"""
Как создать свою базу данных?
- открыть соединение через sqlite3.connect()

Как создать таблицы?
- указать столбцы и типы данных -> CREATE TABLE
- создать первичный ключ -> PRIMARY KEY
- добавить индексы -> CREATE INDEX name_idx ON table_name (column_name)
- добавить ограничения ввода - CONSTRAINT (DEFAULT, CHECK)

Что такое индексы, для чего они нужны и как их создать?
--> CREATE INDEX name_idx ON table_name (column_name)

Как добавить, изменить или удалить данные?
--> INSERT INTO table_name (column_name) VALUES ('column value')
--> UPDATE table_name SET column_name='column_name', column_name='column_name' WHERE id=1
--> DELETE FROM table_name WHERE id=1

"""
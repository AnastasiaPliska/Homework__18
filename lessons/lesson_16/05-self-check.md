# Какой драйвер использовать для PostgreSQL?
psycopg2

# Как соединиться с SQLite БД в файле?
sqlite:///tmp/test.db

# Как соединиться с SQLite БД в памяти?
sqlite:///:memory:  
# в этом случае файлы создаваться не будут и мы каждый раз будем работать с нуля

# Как описать колонку типа String? Integer?
db.Column(db.String)
db.Column(db.Integer)

# Как создать сессию?
Её не надо создавать её можно получить из объекта db
db.session

# Как создать пользователей?
john = User(id=1, name="John", age=30)
kate = User(id=2, name="Kate", age=31)

db.session.add_all([john, kate])
# или
db.session.add(john)
db.session.add(kate)
db.session.commit()

# Как выбрать всех пользователей из таблиц?
User.query.all()

# Как выбрать одного ползователя?
User.query.get(1)   
# где 1 - это конкретный id пользователя

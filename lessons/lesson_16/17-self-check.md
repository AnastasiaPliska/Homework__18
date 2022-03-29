# Какое отношение будет между таблицами User и University?
Один ко многим

# Как выставить NOT NULL-ограничение в SQLAlchemy?
name = db.Column(db.String, nullable=False)

# Как получить всех пользователей, чей возраст больше 18 лет?
users = db.session.query(User).filter(User.age > 18).all()

# Как получить всех пользователей, чье имя начинается с букв Ка?
users = db.session.query(User).filter(User.name.like("Ка%)).all()

# Как удалить строку из таблицы, у которой id = 30?
i = db.session.query(User).get(30)
db.session.delete(i)
db.session.commit()

# Как обновить поле age в строке с id = 3? 
i = db.session.query(User).get(3)
i.age = 21
db.session.add(i)
db.session.commit()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(3), unique=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 18"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")

class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")

db.create_all()

# подготовка данных

group_01 = Group(id=1, name="Group #1")
group_02 = Group(id=2, name="Group #2")

user_01 = User(id=1, name="Kate", age=20, group=group_01)
user_02 = User(id=2, name="Mary", age=22, group=group_01)
user_03 = User(id=3, name="Artur", age=23, group=group_02)
user_04 = User(id=4, name="Yury", age=24, group=group_02)
user_05 = User(id=5, name="Nastya", age=25, group=group_01)
user_06 = User(id=6, name="Leo", age=26, group=group_02)

# работа с транзакциями
with db.session.begin():
    try:
        db.session.add(user_01)
        db.session.add(user_02)

        nested = db.session.begin_nested()
        try:
            db.session.add(user_03)
            db.session.add(user_04)
            # raise Exception("database exception")
            nested.commit()
        except Exception as e:
            print(f"Error: {e}")
            nested.rollback()

        raise Exception("unexcepted exception")

        # db.session.commit()
    except Exception as e:
        db.session.rollback()

print(User.query.all())

if __name__ == "__main__":
    app.run(debug=True)

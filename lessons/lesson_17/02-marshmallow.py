###  Шаг 0 - подготавливаемся  ###

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


###  Шаг 1 - составляем схему  ###

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


###  Шаг 2 - делаем дамп в словарь  ###

# user = User(id=1, name="Jane", age=19)
# user_schema = UserSchema()
# result = user_schema.dump(user)
# print(type(result))
# print(result["name"])


###  Шаг 3 - делаем дамп в строку  ###

user = User(id=1, name="Jane", age=19)
user_schema = UserSchema()
result = user_schema.dumps(user)
print(type(result))
print(result)


###  Шаг 4 - делаем дамп списка  ###

# u1 = User(id=1, name="Jane", age=19)
# u2 = User(id=2, name="John", age=19)
# u3 = User(id=3, name="Kate", age=19)
# u4 = User(id=4, name="Mary", age=19)
#
# users_schema = UserSchema(many=True)
#
# print(users_schema.dump([u1, u2, u3, u4]))
# print(users_schema.dumps([u1, u2, u3, u4]))


###  Шаг 5 - делаем десериализацию

user_json_str = '{"name": "John", "age": 30}'
user_schema = UserSchema()

user_dict = user_schema.loads(user_json_str)
user = User(**user_dict)
print(user.age)


if __name__ == "__main__":
    app.run(debug=True)
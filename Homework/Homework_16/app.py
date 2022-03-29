import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


def user_dict(self):
    return {
        "id": self.id,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "age": self.age,
        "email":self.email,
        "role": self.role,
        "phone": self.phone,
    }


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    orders = db.relationship('Order', foreign_keys=[order_id])
    executors = db.relationship('User', foreign_keys=[executor_id])


def offer_dict(self):
    return {
        "id": self.id,
        "order_id": self.order_id,
        "executor_id": self.executor_id,
    }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    customers = db.relationship('User', foreign_keys=[customer_id])
    executors = db.relationship('User', foreign_keys=[executor_id])


def order_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "start_date": self.start_date,
        "end_date": self.end_date,
        "address": self.address,
        "price": self.price,
        "customer_id": self.customer_id,
        "executor_id": self.executor_id,
    }


db.create_all()


with open('users_data.json', 'r', encoding='utf-8') as f:
    users_info = json.load(f)

all_users = []
for user_data in users_info:
    new_user = User(
        id=user_data["id"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        age=user_data["age"],
        email=user_data["email"],
        role=user_data["role"],
        phone=user_data["phone"],
    )
    all_users.append(new_user)

with db.session.begin():
    db.session.add_all(all_users)


with open('offers_data.json', 'r', encoding='utf-8') as f:
    offers_info = json.load(f)

all_offers = []
for offer_data in offers_info:
    new_offer = Offer(
    id=offer_data["id"],
    order_id=offer_data["order_id"],
    executor_id=offer_data["executor_id"],
    )
    all_offers.append(new_offer)

with db.session.begin():
    db.session.add_all(all_offers)


with open('orders_data.json', 'r', encoding='utf-8') as f:
    orders_info = json.load(f)

all_orders = []
for order_data in orders_info:
    new_order = Order(
    id=order_data["id"],
    name=order_data["name"],
    description=order_data["description"],
    start_date=order_data["start_date"],
    end_date=order_data["end_date"],
    address=order_data["address"],
    price=order_data["price"],
    customer_id=order_data["customer_id"],
    executor_id=order_data["executor_id"],
    )
    all_orders.append(new_order)

with db.session.begin():
    db.session.add_all(all_orders)

db.session.commit()



@app.route("/users", methods=["POST", "GET"])
def get_all_users():
    if request.method == "GET":
        result = []
        users = User.query.all()
        for user in users:
            result.append(user_dict(user))
        return jsonify(result)

    elif request.method == "POST":
        data = request.json
        user = User(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            age=data.get("age"),
            email=data.get("email"),
            role=data.get("role"),
            phone=data.get("phone")
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user_dict(user))


@app.route("/offers", methods=["POST", "GET"])
def get_all_offers():
    if request.method == "GET":
        result = []
        offers = Offer.query.all()
        for offer in offers:
            result.append(offer_dict(offer))
        return jsonify(result)

    elif request.method == "POST":
        data = request.json
        offer = Offer(
            id=data.get("id"),
            order_id=data.get("order_id"),
            executor_id=data.get("executor_id")
        )
        db.session.add(offer)
        db.session.commit()
        return jsonify(offer_dict(offer))


@app.route("/orders", methods=["POST", "GET"])
def get_all_orders():
    if request.method == "GET":
        result = []
        orders = Order.query.all()
        for order in orders:
            result.append(order_dict(order))
        return jsonify(result)

    elif request.method == "POST":
        data = request.json
        order = Order(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            address=data.get("address"),
            price=data.get("price"),
            customer_id=data.get("customer_id"),
            executor_id=data.get("executor_id")
        )
        db.session.add(order)
        db.session.commit()
        return jsonify(order_dict(order))


@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_user(id):
    if request.method == "GET":
        user = User.query.get(id)
        return jsonify(user_dict(user))

    elif request.method == "PUT":
        data = request.json
        user = User(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            age=data.get("age"),
            email=data.get("email"),
            role=data.get("role"),
            phone=data.get("phone")
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user_dict(user))

    elif request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify("")


@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(id):
    if request.method == "GET":
        offer = Offer.query.get(id)
        return jsonify(offer_dict(offer))

    elif request.method == "PUT":
        data = request.json
        offer = Offer(
            id=data.get("id"),
            order_id=data.get("order_id"),
            executor_id=data.get("executor_id")
        )
        db.session.add(offer)
        db.session.commit()
        return jsonify(offer_dict(offer))

    elif request.method == "DELETE":
        offer = Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()
        return jsonify("")


@app.route("/orders/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_order(id):
    if request.method == "GET":
        order = Order.query.get(id)
        return jsonify(order_dict(order))

    elif request.method == "PUT":
        data = request.json
        order = Order(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            address=data.get("address"),
            price=data.get("price"),
            customer_id=data.get("customer_id"),
            executor_id=data.get("executor_id")
        )
        db.session.add(order)
        db.session.commit()
        return jsonify(order_dict(order))

    elif request.method == "DELETE":
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return jsonify("")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Установка инструментария
# pip3 install flask flask-sqlalchemy sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
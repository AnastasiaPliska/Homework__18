from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('demo2.html')

@app.route('/form', methods=["POST"])
def accept_form():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Привет {username}, ваш {password} надежно зашифрован"

app.run()
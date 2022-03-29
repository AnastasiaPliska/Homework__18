from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('demo1.html')

@app.route('/form')
def accept_form():
    phone = request.args.get('phone')
    return f"Ваш телефон: {phone}"

app.run()
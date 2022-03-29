from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo3")
def demo3():
    friends = ["Boris Jonson", "Bill Gates", "Stiv Jobs"]
    return render_template('demo3.html', friends=friends)

app.run(debug=True)

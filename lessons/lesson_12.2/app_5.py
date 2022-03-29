from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo5")
def demo5():
    skills = {
        "Python": "Expert",
        "Flask": "Master",
        "JavaScript": "God"
    }
    return render_template('demo5.html', skills=skills)

app.run(debug=True)

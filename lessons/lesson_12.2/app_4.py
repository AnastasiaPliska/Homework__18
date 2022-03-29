from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo4")
def demo4():
    skills = {
        "Python": "Expert",
        "Flask": "Master",
        "JavaScript": "God"
    }
    return render_template('demo4.html', skills=skills)

app.run(debug=True)

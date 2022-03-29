from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo2")
def demo2():
    offers = 1341435
    cv_published = True
    return render_template('demo2.html', offers=offers, cv_published=cv_published)

app.run(debug=True)

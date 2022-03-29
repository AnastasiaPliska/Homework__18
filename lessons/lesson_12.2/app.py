from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo1")
def demo1():
    skill = "flask, python, html"
    number_of_skills = len(skill.split(","))
    return render_template("demo1.html", name="Вася Пупкин", photo="https://img.lovepik.com/original_origin_pic/18/04/12/035f9d68b99fbe503cdb1c8e7ecda6b3.png_wh860.png", skill = skill, number_of_skills=number_of_skills)



app.run(debug=True)

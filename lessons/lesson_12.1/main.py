from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def page_index():
    # with open("index.html") as f:
    #     page_content = f.read()
    # return page_content
    return redirect("https://ya.ru", code=302)

@app.route("/profile/<id>")
def profile_page(id):
    return f"profile page. User {id}"

@app.route("/groups/<int:id>")
def groups_page(id):
    return f"Groups page. Group {id}"

@app.route("/search")
def search_page():
    search = request.args.get("s")
    return f"looking for {search}"

@app.errorhandler(404)
def page_not_found(e):
    return "ничего я не нашел", 404
# app.add_url_rule("/", view_func=page_index)  - это старая версия написания, сейчас более новая, написана выше: @app.route("/")

app.run()
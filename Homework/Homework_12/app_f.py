from flask import Flask, render_template, request
from utils import get_candidates, load_settings, get_candidate_by_id

app = Flask(__name__)


@app.route('/')
def page_index():
    settings = load_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"

    app.run()


@app.route('/candidate/<int:c_id>/')
def page_candidates(c_id):

    candidate = get_candidate_by_id(c_id)


    information = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src="{candidate["picture"]}" width=200/>
    <p>{candidate["skills"]}</p>
    """

    return information

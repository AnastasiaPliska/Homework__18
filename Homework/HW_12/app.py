from flask import Flask, render_template, request
from utils import get_candidates, load_settings

app = Flask(__name__)


@app.route("/")
def page_index():
    settings = load_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"

app.run(debug=True)
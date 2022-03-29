from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["POST"])
def get_json_data():
    json_data = request.get_json()
    print(json_data)
    return json.dumps('{"success": "true"}')

app.run()
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/', methods=["POST"])
def get_json_data():
    json_data = request.get_json()
    print(json_data)
    response = Response(json.dumps('{"success": "true"}'), content_type = 'application/json')
    return response


app.run()

from flask import Flask
from flask import jsonify

from db import get_tasks

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    d = {"tasks": get_tasks()}
    return jsonify(d)

app.run()

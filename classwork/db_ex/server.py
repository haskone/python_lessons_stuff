from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import request

from db import get_tasks, make_task, update_task

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    d = {"tasks": get_tasks()}
    return jsonify(d)


@app.route('/', methods=['POST'])
def post():
    name = request.get_json(silent=True)['name']
    desc = request.get_json(silent=True)['desc']
    priority = request.get_json(silent=True)['priority']

    make_task(name=name,
              desc=desc,
              exec_time=datetime.utcnow(),
              priority=priority)

    d = {"status": "OK"}
    return jsonify(d)


@app.route('/', methods=['PUT'])
def put():
    if update_task(
            name=request.get_json(silent=True)["name"],
            desc="UPDATED",
            exec_time=datetime(2018, 2, 1, 17, 18, 3, 199474),        
            priority=2):
        d = {"status": "OK"}        
    else:
        d = {"status": "FAIL", "desc": "Not Found"}

    return jsonify(d) 


@app.route('/', methods=['DELETE'])
def delete():
    print(request.get_json(silent=True))
    return ""

app.run()

"""
Server API with using our db module.
"""
from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import request

from db import (
    get_tasks,
    make_task,
    update_task,
    delete_task,
)

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def api_get_tasks():
    d = {"tasks": get_tasks()}
    return jsonify(d)


@app.route('/users', methods=['GET'])
def api_get_users():
    """
    TODO: should be implemented with TinyDB
    """
    d = {"users": []}
    return jsonify(d)


@app.route('/tasks', methods=['POST'])
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


@app.route('/tasks', methods=['PUT'])
def put():
    if update_task(
            name=request.get_json(silent=True)["name"],
            desc="UPDATED",
            exec_time=datetime(1970, 2, 1, 17, 18, 3, 199474),
            priority=2):
        d = {"status": "UPDATED"}
    else:
        d = {"status": "FAIL", "desc": "Not Found"}

    return jsonify(d)


@app.route('/tasks', methods=['DELETE'])
def delete():
    if delete_task(
            name=request.get_json(silent=True)["name"]):
        d = {"status": "DELETED"}
    else:
        d = {"status": "FAIL", "desc": "Not Found"}

    return jsonify(d)


if __name__ == "__main__":
    app.run()

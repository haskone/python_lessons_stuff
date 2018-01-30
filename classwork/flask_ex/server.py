from flask import Flask, session
from flask import jsonify
from flask import request

app = Flask(__name__)
app.secret_key = 'lksikfdjglfjdlkjk'

@app.route('/')
def index():
    return 'Index Page'

from flask import make_response

@app.route('/cookie_add/<user>')
def cookie_add(user):
    resp = make_response("OK, %s added" % user)
    resp.set_cookie(user, "added")
    return resp

@app.route('/cookie_get')
def cookie_get():
    return "Got: %s" % request.cookies.items()

@app.route('/cookie_del/<user>')
def cookie_del(user):
    resp = make_response("Del, %s" % user)
    resp.set_cookie(user, '', expires=0)
    return resp

@app.route('/session_add/<u>')
def ses_1(u):
    session[u] = True
    return "OK: session: %s" % session.keys()

@app.route('/session_get')
def ses_2():
    return "Curr session: %s" % session.keys()

@app.route('/session_delete/<u>')
def ses_3(u):
    del session[u]
    return "Curr session: %s" % session.keys()

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/json')
def summary():
    d = {"key": "value"}
    return jsonify(d)

@app.route('/user/<username>')
def show_user_profile(username):    
    user = request.args.get('username')
    session["username"] = user
    return "OK"

@app.route('/user')
def show_usera_args():
    user = request.args.get('username')
    session[user] = True
    return "OK: %s" % session

@app.route('/sessions')
def get_sessions():
    return "%s / %s / %s" % (session.get("username", "NOTHING"),
                             session.keys(),
                             session)

@app.route('/post_test', methods=["POST"])
def post_test():
    return "got: %s" % request.form['key']

@app.route('/delete_test/<username>', methods=["DELETE"])
def delete_test(username):
    return "got: %s" % username    

if __name__ == '__main__':
    app.run()
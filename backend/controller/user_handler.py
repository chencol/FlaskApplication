import jwt
from flask import request, jsonify, session
from backend import app
from backend.models import User


@app.route('/verify_user', methods=['GET', 'POST'])
def verify_user():
    session.permanent = True
    # username = request.args.get("name")
    username = request.form.get('name')
    # password = request.args.get("password")
    password = request.form.get('password')
    # user = User.query.filter(User.name==username).first()
    user = User.query.filter_by(name=username).first()
    #There is difference between filter and filter by!
    if user==None:
        result = "false"
        return jsonify(result=result)
    else:
        if user.pwd == password:
            b_token = jwt.encode({"username":username},'secret', algorithm='HS256')
            session["username"] = username
            session["token"] = b_token.decode("utf-8")
            result = "true"
            return jsonify(result=result, username=username, token=b_token.decode("utf-8"))
        else:
            result = "false"
            return jsonify(result=result, name=username)

@app.route('/access_control')
def access_control():
    session_token = session.get("token")
    frontend_token = request.args.get("token")
    print(session.get("token"))
    print(session.get("username"))
    if session_token==frontend_token:
        print("User is verified!")
        result = "true"
    else:
        print("User is not verified!")
        result = "false"
    return jsonify(result=result)

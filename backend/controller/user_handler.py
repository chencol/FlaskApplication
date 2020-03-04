import jwt
from flask import request, jsonify, session

from backend import app
from backend.models import User


@app.route('/verify_user')
def verify_user():

    username = request.args.get("name")
    password = request.args.get("password")
    # user = User.query.filter(User.name==username).first()
    user = User.query.filter_by(name=username).first()
    #There is difference between filter and filter by!

    if user==None:
        result = "false"
        return jsonify(result=result, name=username)
    else:
        if user.pwd == password:
            # token = str(jwt.encode({"username":username}, 'secret', algorithm='HS256'))
            b_token = jwt.encode({"username":username}, 'secret', algorithm='HS256')
            # print("Token: " + token)
            # b_token = bytes(token, 'utf-8')
            # print(type(b_token))
            # u_token = jwt.decode(b_token, 'secret', algorithms=['HS256'])
            session["username"] = username
            session["token"] = b_token
            result = "true"
            return jsonify(result=result, username=username, token=str(b_token))

        else:
            result = "false"
            return jsonify(result=result, name=username)


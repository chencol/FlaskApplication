import os
from datetime import timedelta

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.debug = True
app.config.from_object(__name__)
# app.config["SECRET_KEY"] = os.urandom(24)
# app.config["SECRET_KEY"] = "testingsession"
# app.secret_key = "DragonFire"
app.secret_key = 'why would I tell you my secret key?'
CORS(app,supports_credentials=True)

from backend import views
from backend.controller import user_handler

from flask_sqlalchemy import SQLAlchemy

from Backend import app

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/flask1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)

    def __repr__(self):
        return "User with name " + self.name

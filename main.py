from sys import platform

from backend import app
from backend.models import db

if __name__ == "__main__":
    db.create_all()
    app.run()

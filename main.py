from sys import platform

from Backend import app
from Backend.models import db

if __name__ == "__main__":
    db.create_all()
    app.run()

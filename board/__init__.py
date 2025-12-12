import os

from flask import Flask
from dotenv import load_dotenv

from board import pages
from .database import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("Database created!")

    app.register_blueprint(pages.bp)
    
    return app
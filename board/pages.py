from flask import Blueprint, render_template, redirect, request, url_for, flash
from sqlalchemy.exc import IntegrityError

from .database import Song, db

bp = Blueprint("pages", __name__)


@bp.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        new_song = Song(
            number = int(request.form["number"]),
            title = request.form["titel"],
            artist = request.form["interpret"],
            folder = request.form["folder"]
        )
        try:
            db.session.add(new_song)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Fehler: Die Nummer existiert bereits!", "danger")
    songs = Song.query.order_by(Song.number).all()
    return render_template("pages/home.html", songs=songs)


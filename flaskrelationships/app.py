from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import create.py

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@35.242.152.17:3306/games"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
class GameSeries(db.Model):
    series_id = db.Column(db.Integer, primary_key=True)
    series_name = db.Column(db.String(50), nullable=False, unique=True)
    review = db.Column(db.String(50))
    games = db.relationship("Game", backref="seriesname")

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #series = db.Column(db.Integer, db.ForeignKey("game_series.series_id"))
    series = db.Column(db.String(50), db.ForeignKey("game_series.series_name"))





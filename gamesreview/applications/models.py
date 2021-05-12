from applications import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SeriesForm(FlaskForm):
    series_name = StringField('Series Name')
    review = StringField('Review e.g."2/10"')
    submit = SubmitField('add series')

class GameSeries(db.Model):
    series_id = db.Column(db.Integer, primary_key=True)
    series_name = db.Column(db.String(50), nullable=False, unique=True)
    review = db.Column(db.String(50))
    games = db.relationship("Game", backref="seriesname")

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    series = db.Column(db.String(50), db.ForeignKey("game_series.series_name"))
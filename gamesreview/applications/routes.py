from applications import app, db
from applications.models import Game, GameSeries
from flask import render_template

@app.route('/add/<game>')
def add(game):
    new_game = Game(name=game)
    db.session.add(new_game)
    db.session.commit()
    return f"Added {game} to database"

@app.route('/read')
def read():
    all_games = Game.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string
    
@app.route('/readseries')
def readseries():
    all_gameseries = GameSeries.query.all()
    games_string = ""
    for series in all_gameseries:
        games_string += f"<br>{series.series_name}  {series.review}"
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Game.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/rshtml')
def rshtml():
    return render_template("gameseries.html", all_gameseries = GameSeries.query.all() )


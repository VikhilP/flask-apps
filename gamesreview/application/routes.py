from application import app, db
from application.models import Game, GameSeries

@app.route('/add/<game>')
def add(game):
    new_game = Games(name=game)
    db.session.add(new_game)
    db.session.commit()
    return f"Added {game} to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name
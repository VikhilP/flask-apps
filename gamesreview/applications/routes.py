from applications import app, db
from applications.models import Game, GameSeries, SeriesForm
from flask import render_template, request, redirect, url_for

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

@app.route('/', methods= ["GET","POST"])
def gameseriessubmit():
    error = ""
    form = SeriesForm()

    if request.method == "POST":
        series_name = form.series_name.data
        review = form.review.data

        if len(series_name) == 0:
            error = "Please enter the series name"
        else:
            new_series = GameSeries(series_name = form.series_name.data, review = form.review.data)
            db.session.add(new_series)
            db.session.commit()
            return redirect(url_for("readseries"))
    
    return render_template('home.html', form=form, message=error)

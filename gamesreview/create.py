from application import db, models

db.drop_all()
db.create_all()
gameseries_yakuza = models.GameSeries(series_name = "Yakuza", review = "9/10")
db.session.add(gameseries_yakuza)
db.session.commit() #commit here so i can use GameSeries.query.filter_by(series_name='Yakuza').first().series_name other wise it won't search through it


# print(game_yakuza1.seriesname.review)


# db.session.add(gameseries_yakuza)


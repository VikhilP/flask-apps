from app import db, GameSeries, Game

db.drop_all()
db.create_all()
gameseries_yakuza = GameSeries(series_name = "Yakuza", review = "9/10")
db.session.add(gameseries_yakuza)
db.session.commit() #commit here so i can use GameSeries.query.filter_by(series_name='Yakuza').first().series_name other wise it won't search through it


game_yakuza0 = Game(name = "Yakuza 0", seriesname = gameseries_yakuza)
game_yakuza1 = Game(name = "Yakuza Kiwami", series = GameSeries.query.filter_by(series_name='Yakuza').first().series_name)

# print(game_yakuza1.seriesname.review)


# db.session.add(gameseries_yakuza)

db.session.add(game_yakuza0)
db.session.add(game_yakuza1)

db.session.commit()
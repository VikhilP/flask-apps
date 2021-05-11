from app import db, GameSeries, Game

db.drop_all()
db.create_all()
gameseries_yakuza = GameSeries(series_name = "Yakuza", review = "9/10")
game_yakuza0 = Game(name = "Yakuza 0", series = 1)
game_yakuza1 = Game(name = "Yakuza Kiwami", series = 1)


db.session.add(gameseries_yakuza)

db.session.add(game_yakuza0)
db.session.add(game_yakuza1)

db.session.commit()
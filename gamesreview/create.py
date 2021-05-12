from applications import db, models

db.drop_all()
db.create_all()
gameseries_1 = models.GameSeries(series_name = "Doom", review = "9/10")
db.session.add(gameseries_1)
db.session.commit() 



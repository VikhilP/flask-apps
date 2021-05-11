from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Vikhil',last_name='parshotam') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()

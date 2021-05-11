from app import db, Todo

db.drop_all()
db.create_all()

todo1 = Todo(task = "Sleep with the fishes")
todo2 = Todo(task ="Buy some malk")
todo3 = Todo(task = "LETS GO", complete = True)

db.session.add(todo1)
db.session.add(todo2)
db.session.add(todo3)

db.session.commit()


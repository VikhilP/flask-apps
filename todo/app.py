from flask import Flask
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@35.242.152.17:3306/todos"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable = False)
    complete = db.Column(db.Boolean, default = False)

@app.route('/')
def index():
    return "This is a TODO list"

@app.route("/todos")
def readtodos():
    all_todos = Todo.query.all()
    todo_sum = ""
    for todo in all_todos:
        todo_sum = todo_sum + "<br>" + todo.task + " " + str(todo.complete)
    return todo_sum

@app.route("/add/<tasks>")
def addtodos(tasks):
    new_todo = Todo(task=tasks)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("readtodos"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
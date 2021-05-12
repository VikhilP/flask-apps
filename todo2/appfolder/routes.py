from appfolder import app, db
from appfolder.models import Todos, TodoForm
from flask import render_template, request, redirect, url_for

@app.route('/add/<todo>')
def add(todo):
    new_todo = Todos(task=todo)
    db.session.add(new_todo)
    db.session.commit()
    return f"Added {todo} to todo list"

@app.route('/complete/<todoid>')
def complete(todoid):
    # temp = Todos.query.filter_by(id=todoid).first()
    if Todos.query.get(int(todoid)) is not None:
        temp = Todos.query.get(int(todoid))
        temp.done = True
        db.session.commit()
        return f"{temp.task} is complete"
    return "error"
    

@app.route('/delete/<todoid>')
def delete(todoid):
    temp = Todos.query.get(int(todoid))
    temptask = temp.task
    db.session.delete(temp)
    db.session.commit()
    return f"{temptask} has been deleted"

@app.route('/')
def index():
    return render_template("index.html", all_todos = Todos.query.all() )

@app.route("/addform", methods = ["GET", "POST"])
def addform():
    error = ""
    form = TodoForm()

    if request.method == "POST":
        _task = form.task.data

        if len(_task) ==0:
            error = "Please enter data to add"
        else:
            new_todo = Todos(task = _task)
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for("index"))
        
    return render_template('add.html', form=form, message = error)



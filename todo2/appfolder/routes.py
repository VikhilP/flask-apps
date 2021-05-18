from appfolder import app, db
from appfolder.models import Todos, TodoForm, IndexForm
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

@app.route('/complete', methods = ["POST"])
def complete2():
    temp = request.form.get("id")
    temptask = Todos.query.filter_by(id=temp).first()
    temptask.done = True
    db.session.commit()
    return redirect("/")

@app.route('/incomplete', methods = ["POST"])
def incomplete():
    temp = request.form.get("id")
    temptask = Todos.query.filter_by(id=temp).first()
    temptask.done = False
    db.session.commit()
    return redirect(url_for("index"))
    

@app.route('/delete', methods=["POST"])
def delete2():
    temp = request.form.get("id")
    temptask = Todos.query.filter_by(id=temp).first()
    db.session.delete(temptask)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<todoid>')
def delete(todoid):
    temp = Todos.query.get(int(todoid))
    temptask = temp.task
    db.session.delete(temp)
    db.session.commit()
    return f"{temptask} has been deleted"

@app.route('/', methods = ["GET", "POST"])
def index():
    form = IndexForm()
    return render_template("index.html", form=form, all_todos = Todos.query.all() )


@app.route("/update", methods = ["GET", "POST"])
def update():
    error = ""
    temp = request.form.get("id")
    temptask = Todos.query.filter_by(id=temp).first()
    form = TodoForm()
    # form.task.data = temptask.task

    if request.method == "POST":
        _task = form.task.data

        if len(_task) ==0:
            error = "You cannot update data to be Null"
        else:
            temptask.task = _task
            db.session.commit()
            return redirect(url_for("index"))
    elif request.method == "GET":
        form.task.data = temptask.task
        
    return render_template('update.html', form=form, message = error, todo = temptask)

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



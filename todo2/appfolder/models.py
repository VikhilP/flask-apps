from appfolder import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(50), nullable = False)
    done = db.Column(db.Boolean, default = False)

class TodoForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Todo')


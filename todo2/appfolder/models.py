from wtforms.fields.core import SelectField
from appfolder import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(50), nullable = False)
    done = db.Column(db.Boolean, default = False)

class TodoForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Todo')

class IndexForm(FlaskForm):
    changestate = SelectField("Change Status", choices=[("complete","complete"), ("incomplete", "incomplete")])
    delete = SubmitField("Delete Task")
    save = SubmitField("Save Changes")
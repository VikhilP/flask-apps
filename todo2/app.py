from flask import Flask, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from appfolder import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
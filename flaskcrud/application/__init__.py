from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@35.242.152.17:3306/gametest"

db = SQLAlchemy(app)

from application import routes
from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@35.242.152.17:3306/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Users(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)



if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")
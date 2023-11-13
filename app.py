from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    residentName = db.Column(db.String(120), nullable=False)
    dateOfBirth = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<firstName %r>'% self.firstName



@app.route("/")
def admin():
    return render_template('admin.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/register")
def register():
  return render_template('register.html')


@app.route("/check")
def check():
  return render_template('check.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
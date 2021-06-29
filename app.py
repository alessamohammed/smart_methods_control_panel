import json
import dateutil.parser 
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler


# App Config.

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# connect to a local postgresql database
migrate = Migrate(app, db)

class Engines(db.Model):
    __tablename__ = 'Engines'

    id = db.Column(db.Integer, primary_key=True)
    Engine1 = db.Column(db.Integer, nullable=False)
    Engine2 = db.Column(db.Integer, nullable=False)
    Engine3 = db.Column(db.Integer, nullable=False)
    Engine4 = db.Column(db.Integer, nullable=False)
    Engine5 = db.Column(db.Integer, nullable=False)
    Engine6 = db.Column(db.Integer, nullable=False)


@app.route('/')
def index(): 
    return render_template('index.html')

    

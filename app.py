
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
# App Config.

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/smart_methods'
db = SQLAlchemy(app)
print(db)
# connect to a local mysql database
#migrate = Migrate(app, db)

class Engines(db.Model):
    __tablename__ = 'Engines'

    id = db.Column(db.Integer, primary_key=True)
    Engine1 = db.Column(db.Integer, nullable=False)
    Engine2 = db.Column(db.Integer, nullable=False)
    Engine3 = db.Column(db.Integer, nullable=False)
    Engine4 = db.Column(db.Integer, nullable=False)
    Engine5 = db.Column(db.Integer, nullable=False)
    Engine6 = db.Column(db.Integer, nullable=False)

#db.create_all()
@app.route('/engines/create')
def engines_submit():
    Engine1 = request.get_json()['enginevalue1']
    Engine2 = request.get_json()['enginevalue2']
    Engine3 = request.get_json()['enginevalue3']
    Engine4 = request.get_json()['enginevalue4']
    Engine5 = request.get_json()['enginevalue5']
    Engine6 = request.get_json()['enginevalue6']

    Engine = Engines(Engine1=Engine1,Engine2=Engine2,Engine3=Engine3,Engine4=Engine4,Engine5=Engine5,Engine6=Engine6)
    db.session.add(Engine)
    db.session.commit()


@app.route('/')
def index(): 
    return render_template('index.html')

    

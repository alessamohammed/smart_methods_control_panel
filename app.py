
from flask import Flask, render_template, request,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import sys
# App Config.

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# connect to a local mysql database
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

class Remote(db.Model):
    __tablename__ = 'Remote'

    id = db.Column(db.Integer, primary_key=True)
    Direction = db.Column(db.String(10))


@app.route('/engines/create', methods=['POST'])
def engines_submit():
    error = False
    default_value='0'
    try:
        Engine1 = request.form.get('enginevalue1',default_value)
        Engine2 = request.form.get('enginevalue2',default_value)
        Engine3 = request.form.get('enginevalue3',default_value)
        Engine4 = request.form.get('enginevalue4',default_value)
        Engine5 = request.form.get('enginevalue5',default_value)
        Engine6 = request.form.get('enginevalue6',default_value)
        Engine = Engines(Engine1=Engine1,Engine2=Engine2,Engine3=Engine3,Engine4=Engine4,Engine5=Engine5,Engine6=Engine6)
        db.session.add(Engine)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return render_template('index.html')+'<p>values were inserted successfully</p>'


@app.route('/engines/values/table')
def engine_values(): 
    return render_template('enginevalues.html',Engines=Engines.query.all())

@app.route('/remote')
def remote():
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/forward', methods=['POST'])
def forward():
    error = False
    try:
        Direction = 'Forward'
        remote = Remote(Direction=Direction)
        db.session.add(remote)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/backward', methods=['POST'])
def backward():
    error = False
    try:
        Direction = 'Backward'
        remote = Remote(Direction=Direction)
        db.session.add(remote)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/left', methods=['POST'])
def left():
    error = False
    try:
        Direction = 'Left'
        remote = Remote(Direction=Direction)
        db.session.add(remote)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/right', methods=['POST'])
def right():
    error = False
    try:
        Direction = 'Right'
        remote = Remote(Direction=Direction)
        db.session.add(remote)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/stop', methods=['POST'])
def stop():
    error = False
    try:
        Direction = 'Stop'
        remote = Remote(Direction=Direction)
        db.session.add(remote)
        db.session.commit()   
        
    except():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    return render_template('Remote.html', remotes=Remote.query)

@app.route('/')
def index(): 
    return render_template('index.html')

    

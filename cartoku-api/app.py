from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSON
from config import Config
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

## MODELS

class App(db.Model):
    __tablename__ = 'apps'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    oauth_client_id = db.Column(db.String(), nullable=False)
    oauth_client_secret = db.Column(db.String(), nullable=False)

class Deploy(db.Model):
    __tablename__ = 'deploys'

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey("apps.id"), nullable=False)
    status = db.Column(db.String(), nullable=False)

    def __init__(self, app, status):
        self.app = app
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)


## ROUTES

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<username>/apps/<string:app_name>/deploy', methods=['POST'])
def push_deploy(username, app_name):
#    import pdb; pdb.set_trace()
    status = request.form['status']
    deploy = Deploy(app_name, status)
    return jsonify(
                {'status': 'ok'}
            )


@app.route('/<username>/deploys/<int:deploy_id>', methods=['GET'])
def show_deploy(username, deploy_id):
    pass

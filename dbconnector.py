import sys
import logging
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from configuration import get_config
app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
mongodb_db = get_config(parameter_type='db-params', parameter_name='MONGODB_DB')
mongodb_uri = get_config(parameter_type='db-params', parameter_name='MONGODB_URI')
mongodb_user = get_config(parameter_type='db-params', parameter_name='MONGODB_USER')
mongodb_pass = get_config(parameter_type='db-params', parameter_name='MONGODB_PASS')
mongodb_connection_string = 'mongodb://' + mongodb_user + ':' + mongodb_pass + '@' + mongodb_uri + '/' + mongodb_db

logging.debug('This is the db: ' + mongodb_db + ' This is the uri: '
      + mongodb_uri + ' This is the user: ' + mongodb_user + ' This is the password: ' + mongodb_pass)

app.config['MONGOALCHEMY_DATABASE'] = mongodb_db
app.config['MONGOALCHEMY_CONNECTION_STRING'] = mongodb_connection_string
db = MongoAlchemy(app)


class Connector(db.Document):
    tok_id = db.StringField()
    tok_tag = db.StringField()
    tok_location = db.StringField()
    tok_date = db.DateTimeField()
    tok_file = db.StringField()


class RandomTok(db.Document):
    pass
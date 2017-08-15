import sys
import logging
from flask import Flask
from mongoengine import *
from configuration import get_config
app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
mongodb_db = get_config(parameter_type='db-params', parameter_name='MONGODB_DB')
mongodb_uri = get_config(parameter_type='db-params', parameter_name='MONGODB_URI')
mongodb_port = get_config(parameter_type='db-params', parameter_name='MONGODB_PORT')
mongodb_user = get_config(parameter_type='db-params', parameter_name='MONGODB_USER')
mongodb_pass = get_config(parameter_type='db-params', parameter_name='MONGODB_PASS')
mongodb_connection_string = 'mongodb://' + mongodb_user + ':' + mongodb_pass + '@' + mongodb_uri + '/' + mongodb_db

logging.debug('This is the db: ' + mongodb_db + ' This is the uri: '
      + mongodb_uri + ' This is the user: ' + mongodb_user + ' This is the password: ' + mongodb_pass)

connect('experiments', host=mongodb_uri)


class Tok(Document):
    tok_id = StringField()
    tok_tag = StringField()
    tok_location = StringField()
    tok_date = DateTimeField()
    tok_file = StringField()
    tok_stamp = StringField()


class Counter(Document):
    tok_tag = StringField()
    pass


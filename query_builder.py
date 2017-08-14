from dbconnector import Connector, RandomTok

from datetime import datetime
import random
import uuid
from faker import Factory


date = datetime.now()
tok_id = str(uuid.uuid4())
faker_location = Factory.create()
location = str(faker_location.city())


def save_query(tok_tag, tok_location, tok_file):
    Tok = Connector(tok_date=date, tok_id=tok_id, tok_tag=tok_tag, tok_location=tok_location, tok_file=tok_file)
    Tok.save()


def get_random():
    Tok = RandomTok
    count = Tok.count()
    return Tok.find()[random.randrange(count)]

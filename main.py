from datetime import datetime
import os
import uuid
from bottle import Bottle, request, run, post, get
from query_builder import query

app = Bottle()
date = datetime.now()
tok_id = str(uuid.uuid4())


@get('/')
def index():
    return 'Hi there'


@post('/post_request')
def post_request():
    tok_tag = request.params.get('tok_tag')
    tok_location = request.params.get('tok_location')
    tok_file = request.params.get('tok_file')
    query(tok_tag, tok_location, tok_file)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(debug=True, host='0.0.0.0', port=port, reloadable=True)
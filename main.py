from datetime import datetime
import os
import uuid
from bottle import Bottle, request, run, post, get
from query_builder import save_query, get_random_tok

app = Bottle()
date = datetime.now()
tok_id = str(uuid.uuid4())


@post('/post_request')
def post_request():
    tok_tag = request.params.get('tok_tag')
    tok_location = request.params.get('tok_location')
    tok_file = request.params.get('tok_file')
    save_query(tok_tag, tok_location, tok_file)
    return 'Hi there'


@get('/get_random')
def get_random():
    return {'tok_file': get_random_tok()}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    run(debug=True, host='0.0.0.0', port=port, reloadable=True)
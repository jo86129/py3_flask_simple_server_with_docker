# -*- coding: utf-8 -*-

from flask import Flask
import os
from gevent.pywsgi import WSGIServer
from Other.Activity import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/activity')


@app.get('/')
def hello():
    return 'Hello world'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.config['env'] = os.environ.get('env', 'dev')
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()

import json
import Queue
import threading
import requests
import ConfigParser
import hashlib
from requests_oauthlib import OAuth1
from flask import Flask, render_template, request, make_response
import flask

def get_data(handle):
    pass
app = Flask(__name__)
UPLOAD_FOLDER = './videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/')
# def index():
#     handle = request.args.get('handle')
#     if handle:
#         count = get_data(handle)
#     return render_template('index.html', **locals())
@app.route('/videos/<path:path>', methods=['GET'])
def download_file(path):
    fullpath = "./videos/" + path
    key=request.args.get('key')
    if key:
        gen=hashlib.md5(path).hexdigest()
        if key==gen:
            return flask.send_from_directory(directory='videos', filename=path)
    # return flask.send_from_directory(directory='videos', filename=path)
    return 'Not authorized'
app.run(debug=True)

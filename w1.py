#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
#@app.route('/')

def index():
#    return "Hi, Ha"
#def postjson():
    print(request.is_json)
    print(request)
    content = request.get_json()
    
    print(content)
#    print(content['id'])
#    print(content['name'])
    return content['name']


app.run(host='0.0.0.0', port=5000)
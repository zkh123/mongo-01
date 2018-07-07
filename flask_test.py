# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'hello world'


@app.route("/index")
def index():
    r = requests.get('http://localhost:5000/getData')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    print(r.json())
    name = r.json()['name']
    return render_template('index.html', name=name)


@app.route("/getData")
def getData():
    dict = {'name': '上海'}
    jsonData = json.dumps(dict)
    return jsonData


if __name__ == '__main__':
    app.run(debug=True)

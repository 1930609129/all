# -*- coding:utf-8 -*-
from flask import Flask
import time
app = Flask(__name__)

@app.route('/h')
def h():
    time.sleep(2)
    return 'h'

@app.route('/hh')
def hh():
    time.sleep(2)
    return 'hh'

@app.route('/hhh')
def hhh():
    time.sleep(2)
    return 'hhh'

if __name__ == '__main__':
    app.run(threaded=True)
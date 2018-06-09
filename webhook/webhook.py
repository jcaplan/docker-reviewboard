#!/usr/bin/env python3

from flask import Flask, request
import json
import sys
sys.stdout = sys.stderr

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    print(json.dumps(request.json, indent=2, sort_keys=True))
    return 'OK'

app.run('0.0.0.0', 8081)

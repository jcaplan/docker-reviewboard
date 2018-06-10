#!/usr/bin/env python

from __future__ import print_function
from flask import Flask, request
import json
import sys
from rbtools.api.client import RBClient
from multiprocessing import Process, Queue
import jenkins
import atexit

sys.stdout = sys.stderr
q = Queue()

app = Flask(__name__)
app.debug = True

jenkins_uname = 'admin'
jenkins_pass = 'admin'
jenkins_url = 'http://jenkins:8080'
reviewboard_url = 'http://reviewboard:8000'
api_token = 'f2c55a7ad5e427063cf51dcdd1689b835b2856ae'

def handle_request_publish(data):
    url = data['review_request']['absolute_url']
    jen = jenkins.Jenkins(jenkins_url, username=jenkins_uname, password=jenkins_pass)
    jen.build_job('svn-demo', {'review.url': url})


def handle_review_publish(data):
    if (data['review']['links']['user']['title'] == jenkins_uname and
        'Uh oh' in data['review']['body_top']):
        q.put(data['review_request']['id'])

@app.route('/', methods=['POST'])
def index():
    print(json.dumps(request.json, indent=2, sort_keys=True))
    data = request.json
    if data['event'] == 'review_request_published':
        handle_request_publish(data)
    elif data['event'] == 'review_published':
        handle_review_publish(data)
    return 'OK'


class Worker(Process):
    def run(self):
        while True:
            id = q.get()
            print('WORKER THREAD: build failed for', id)
            client = RBClient(reviewboard_url, api_token=api_token)
            root = client.get_root()
            review = root.get_review_request(review_request_id=id)
            comments = review.get_reviews(max_results=200)

            for c in comments:
                if c.links.user.title == jenkins_uname and c.ship_it:
                    c.update(ship_it=False)


worker = Worker(name ='1')
worker.start()
atexit.register(worker.terminate)
app.run('0.0.0.0', 8081)

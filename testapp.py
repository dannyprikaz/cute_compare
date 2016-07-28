from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import numpy as np
from random import randint
from collections import defaultdict
app = Flask(__name__)

sessions = defaultdict(dict)
cute1 = None
cute2 = None
vote1 = 0
vote2 = 0
mages1 = []
images2 = []
sudden1 = None
sudden2 = None

def random_mammals():
    with open('mammals.txt') as f:
        mammals = f.readlines()
        mammals = [[m.strip('\n')] for m in mammals]
        rand_mammal_1 = mammals[randint(0,len(mammals))]
        rand_mammal_2 = mammals[randint(0,len(mammals))]
    return rand_mammal_1[0], rand_mammal_2[0]

def save_urls(cute1, cute2):
    r1 = requests.get('https://www.google.com/search?tbm=isch&q=cute+{}'.format(cute1))
    r2 = requests.get('https://www.google.com/search?tbm=isch&q=cute+{}'.format(cute2))
    bs1 = BeautifulSoup(r1.content, 'html.parser')
    bs2 = BeautifulSoup(r2.content, 'html.parser')
    global images1, images2, sudden1, sudden2
    images1 = [image['src'] for image in bs1.findAll('img')[:10]]
    images2 = [image['src'] for image in bs2.findAll('img')[:10]]
    sudden1 = bs1.findAll('img')[10]['src']
    sudden2 = bs2.findAll('img')[10]['src']

def fighter():
    global images1, images2, vote1, vote2
    if images1:
        im1 = images1.pop()
        im2 = images2.pop()
        return render_template('fight.html', im1=im1, im2=im2)
    else:
        sudden = ''
        if vote1 == vote2:
            sudden = '/sudden'
        return render_template('result_pause.html', sudden=sudden)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/landing', methods=['POST'])
def landing():
    global cute1, cute2, vote1, vote2, sessions
    vote1, vote2 = 0, 0
    cute1, cute2 = str(request.form['object1']), str(request.form['object2'])
    if not cute1 and not cute2:
        cute1, cute2 = random_mammals()
    elif not cute1:
        cute1, _ = random_mammals()
    elif not cute2:
        _, cute2 = random_mammals()
    save_urls(cute1, cute2)
    return render_template('landing.html', cute1=cute1, cute2=cute2)

@app.route('/fight')
def fight():
    return fighter()

@app.route('/fight/one')
def fight_one():
    global vote1
    vote1 += 1
    return fighter()

@app.route('/fight/two')
def fight_two():
    global vote2
    vote2 += 1
    return fighter()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

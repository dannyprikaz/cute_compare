from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import numpy as np
app = Flask(__name__)

cute1 = None
cute2 = None
images1 = []
images2 = []
sudden1 = None
sudden2 = None
vote1 = 0
vote2 = 0

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


@app.route('/')
def index():
    return render_template('home.html')

# # home page
# @app.route('/')
# def index():
#     return '''
#     <h1> Cute Compare </h1>
#     <form action="/landing" method='POST' >
#     <p>
#         <input type="text" name="object1" />
#     </p>
#     <p>
#         <input type="text" name="object2" />
#         <input type="submit" />
#     </p>
#     </form>
#     '''

@app.route('/results')
def results():
    global cute1, cute2, vote1, vote2
    if vote1 == vote2:
        winner = 'Tie!'
    else:
        winner = [cute1, cute2][np.argmax(np.array([vote1, vote2]))]
    return '''
           <h1>Results</h1>
           <p> {}: {}</p>
           <p> {}: {}</p>
           <h1> Cuteness Champion: {}</h1>
           <a href="/"><button>Battle Again</button></a>
           '''.format(cute1, vote1, cute2, vote2, winner)

@app.route('/results/sudden')
def results_sudden():
    global sudden1, sudden2
    return '''
           <h1>Sudden Death!</h1>
           <a href="/fight/one"><img src="{}" width="200"></img></a>
           <a href="/fight/two"><img src="{}" width="200"></img></a>
           '''.format(sudden1, sudden2)

@app.route('/fight/one')
def fight_one():
    global images1, images2, vote1, vote2
    vote1 += 1
    if images1:
        im1 = images1.pop()
        im2 = images2.pop()
        return '''
               <h1> Cute Compare </h1>
               <a href="/fight/one"><img src="{}" width="200"></img></a>
               <a href="/fight/two"><img src="{}" width="200"></img></a>
               '''.format(im1, im2)
    else:
        sudden = ''
        if vote1 == vote2:
            sudden = '/sudden'
        return '''
               <h1>The battle is over</h1>
               <a href="/results{}"><button>See your results</button></a>
               '''.format(sudden)

@app.route('/fight/two')
def fight_two():
    global images1, images2, vote1, vote2
    vote2 += 1
    if images1:
        im1 = images1.pop()
        im2 = images2.pop()
        return '''
               <h1> Cute Compare </h1>
               <a href="/fight/one"><img src="{}" width="200"></img></a>
               <a href="/fight/two"><img src="{}" width="200"></img></a>
               '''.format(im1, im2)
    else:
        sudden = ''
        if vote1 == vote2:
            sudden = '/sudden'
        return '''
               <h1>The battle is over</h1>
               <a href="/results{}"><button>See your results</button></a>
               '''.format(sudden)

@app.route('/fight')
def fight():
    global images1, images2
    im1 = images1.pop()
    im2 = images2.pop()
    return '''
           <h1> Cute Compare </h1>
           <a href="/fight/one"><img src="{}" width="200"></img></a>
           <a href="/fight/two"><img src="{}" width="200"></img></a>
           '''.format(im1, im2)

# landing page compiles urls for images
@app.route('/landing', methods=['POST'])
def landing():
    global cute1, cute2, vote1, vote2
    vote1, vote2 = 0, 0
    cute1, cute2 = str(request.form['object1']), str(request.form['object2'])
    save_urls(cute1, cute2)
    return '''
           <h1> {} vs. {} </h1>
           <a href="/fight"><button>Commence Battle!</button></a>
           '''.format(cute1, cute2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

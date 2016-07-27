from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
from random import randint

# home page
@app.route('/')
def index():
    return render_template('index.html')

def random_mammals():
    with open('mammals.txt') as f:
        mammals = f.readlines()
        mammals = [[m.strip('\n')] for m in mammals]
        rand_mammal_1 = mammals[randint(0,len(mammals))]
        rand_mammal_2 = mammals[randint(0,len(mammals))]
    return rand_mammal_1, rand_mammal_2

# loads the pickled model and vectorizer
def load_model():
    with open('data/vectorizer.pkl') as f:
        vectorizer = pickle.load(f)
    with open('data/model.pkl') as f:
        model = pickle.load(f)
    return vectorizer, model

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

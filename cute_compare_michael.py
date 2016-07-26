from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
from random import randint

# home page
@app.route('/')
def index():
    return render_template('index.html')
    #
    # '''
    # <h1> Cute Compare </h1>
    # <form action="/predict" method='POST' >
    # <input type="text" name="object1" />
    # <input type="submit" />
    # </form>
    # <form action="/predict" method='POST' >
    # <input type="text" name="object2" />
    # <input type="submit" />
    # </form>
    # '''

def random_mammals()
    with open('mammals.txt') as f:
        mammals = f.readlines()
        mammals = [[m.strip('\n')] for m in mammals]
        rand_mammal_1 = mammals[randint(0,len(mammals))]
        rand_mammal_2 = mammals[randint(0,len(mammals))]
    return rand_mammal_1, rand_mammal_2

# compare page
@app.route('/predict', methods=['POST'])
def predict():
    article = str(request.form['user_input'])
    article_tfidf = vectorizer.fit_transform(article)
    prediction = model.predict(article_tfidf)
    pass

# loads the pickled model and vectorizer
def load_model():
    with open('data/vectorizer.pkl') as f:
        vectorizer = pickle.load(f)
    with open('data/model.pkl') as f:
        model = pickle.load(f)
    return vectorizer, model

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

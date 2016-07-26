from flask import Flask, request
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
    <h1> Cute Compare </h1>
    <form action="/predict" method='POST' >
    <input type="text" name="object1" />
    <input type="submit" />
    </form>
    <form action="/predict" method='POST' >
    <input type="text" name="object2" />
    <input type="submit" />
    </form>
    '''

# compare page
@app.route('/predict', methods=['POST'])
def predict():
    article = str(request.form['user_input'])
    article_tfidf = vectorizer.fit_transform(article)
    prediction = model.predict(article_tfidf)
    return '''


# loads the pickled model and vectorizer
def load_model():
    with open('data/vectorizer.pkl') as f:
        vectorizer = pickle.load(f)
    with open('data/model.pkl') as f:
        model = pickle.load(f)
    return vectorizer, model

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

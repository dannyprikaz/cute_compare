from flask import Flask, request
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
    <h1> Cute Compare </h1>
    <form action="/predict" method='POST' >
    <input type="text" name="object1" />
    <input type="text" name="object2" />
    <input type="submit" />
    </form>
    '''

# compare page
@app.route('/predict', methods=['POST'])
def predict():
    cute1, cute2 = str(request.form['object1']), str(request.form['object2'])
    return '''
           <h1> {} vs. {} </h1>
           '''.format(cute1, cute2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

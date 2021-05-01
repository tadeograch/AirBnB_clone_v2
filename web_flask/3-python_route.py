#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Display Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    '''Display C followed by the value of the text variable'''
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable(text="is cool"):
    '''Display Python followed by the value of the text variable'''
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

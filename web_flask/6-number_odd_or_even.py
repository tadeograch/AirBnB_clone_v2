#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, escape, render_template

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
    return "C {}".format(escape(new_text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable(text="is cool"):
    '''Display Python followed by the value of the text variable'''
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_variable(n):
    '''Display n is a number only if n is an integer'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Display a HTML page only if n is an integer'''
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>)', strict_slashes=False)
def number_odd_or_even(n):
    '''Display a HTML page only if n is an integer'''
    if (n % 2 == 0):
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

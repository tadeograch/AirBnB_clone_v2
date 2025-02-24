#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Display a HTML page'''
    s_list = storage.all(State).values()
    return render_template("8-cities_by_states.html", s_list=s_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''Remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

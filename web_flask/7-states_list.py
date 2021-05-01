#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Display a HTML page'''
    s_list = storage.all(State).values()
    return render_template("7-states_list.html", s_list=s_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''Remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

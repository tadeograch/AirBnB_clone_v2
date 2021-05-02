#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id_cities(id):
    '''Display a HTML page'''
    s_list = storage.all(State).values()
    return render_template("9-states.html", s_list=s_list, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    '''Remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
'''Starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''Display a HTML page'''
    s_list = storage.all(State).values()
    a_list = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", s_list=s_list, a_list=a_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''Remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == '__main__':
    '''Listening on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)

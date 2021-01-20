#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage():
    """ Remove the current SQLAlchemy Session. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """ List States. """
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)

    return render_template('7-states_list.html', slist=states)

if __name__ == '__main__':
    app.run()

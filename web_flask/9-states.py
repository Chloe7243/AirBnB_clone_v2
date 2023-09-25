#!/usr/bin/python3
""" Web Flask """
from models import storage
from flask import Flask, request, render_template
from models.state import State
from models.city import City

app = Flask(__name__, template_folder='templates')


@app.teardown_appcontext
def teardown_db(e):
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states/', strict_slashes=False)
def states(id=None):
    c = 1
    states = list(storage.all(State).values())
    state = None
    if id is not None:
        c = 2
        for state in states:
            if state.id == id:
                state = state
                break
    return render_template('9-states.html', c=c, stat=states, state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

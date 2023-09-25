#!/usr/bin/python3
""" Web Flask """
from models import storage
from flask import Flask, request, render_template
from models.state import State

app = Flask(__name__, template_folder='templates')


@app.teardown_appcontext
def teardown_db(e):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

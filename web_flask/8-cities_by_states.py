#!/usr/bin/python3
"""starts a flask web app"""

from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)
application.url_map.strict_slashes = False


@application.teardown_appcontext
def teardown_appcontext(self):
    """close and reload the storage between requests"""
    storage.close()


@application.route('/cities_by_states')
def showStatesCities():
    """List all the stored states and their cities"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)

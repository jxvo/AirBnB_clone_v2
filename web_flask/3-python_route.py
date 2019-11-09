#!/usr/bin/python3
""" Starts a Flask Web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns hello HBNB """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def txt(text):
    """ returns C with text variable value """
    text = text.replace('_', ' ')
    return('C %s' % (text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):
    """ returns Python with text variable value """
    text = text.replace('_', ' ')
    return('Python %s' % (text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

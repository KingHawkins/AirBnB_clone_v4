#!/usr/bin/python3
"""
GETS 'text' via http request  and displays it in a page
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """the index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """The first route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """checks if text a string"""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
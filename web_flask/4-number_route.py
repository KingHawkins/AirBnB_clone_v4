#!/usr/bin/python3
"""
uses the GET request and checks parameter passed
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """first route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """checks if text is string"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """provides 3 options for routing"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """checks if n is an integer and displays it"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

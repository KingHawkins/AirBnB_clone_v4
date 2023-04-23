#!/usr/bin/python3
"""checks if parameter passed is an integer and whether is even or odd
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """home page"""
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
    """cheks if n is a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numtemplate(n):
    """checks if n is integer"""
    return render_template('5-number.html', number=n, title="HBNB")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

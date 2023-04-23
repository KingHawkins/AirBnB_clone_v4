#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def display():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text(text):
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    return f"Python {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


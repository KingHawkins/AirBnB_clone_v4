#!/usr/bin/python3
from flask import Flask
"""
This is the first task in flask.
we are to display the index page.
"""
app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000

@app.route('/', strict_slashes=False)
def index():
    """The index page"""
    return "Hello HBNB"

if __name__ == '__main__':
    app.run(debug=True)

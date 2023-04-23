from flask import Flask, render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def numtemplate(n):
    return render_template('5-number_template.html', number=n, title="HBNB")

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    return render_template('6-number_odd_or_even.html', number=n, title="HBNB")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
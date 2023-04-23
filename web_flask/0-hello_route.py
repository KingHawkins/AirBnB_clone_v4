from flask import Flask

app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB"

if __name__ == '__main__':
    app.run(debug=True)

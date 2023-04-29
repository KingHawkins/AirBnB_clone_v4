#!/usr/bin/python3
"""
Contains routes for all the objects.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def custom_404(error):
    """handles bad request 404"""
    return jsonify(error="Not found")


@app.teardown_appcontext
def close(exception):
    """closes the connection to database"""
    storage.close()


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
    PORT = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000

    app.run(debug=True, host=HOST, port=PORT, threaded=True)

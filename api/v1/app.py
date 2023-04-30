#!/usr/bin/python3
"""
Contains routes for all the objects.
"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv
from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "Flasgger",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "1.0",
            "title": "HBNB API",
            "endpoint": 'v1_views',
            "description": 'HBNB REST API',
            "route": '/v1/views',
        }
    ]
}
swagger = Swagger(app)

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

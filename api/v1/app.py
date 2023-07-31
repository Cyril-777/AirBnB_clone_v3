#!/usr/bin/python3
"""the api application"""
from flask import Flask, make_response, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
CORS(app, resources={'/*': {'origins': "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on teardown."""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """404 page not found handling"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")

    app.run(host=host, port=port, threaded=True)

#!/usr/bin/python3
"""
This is the status view.
"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def return_status():
    """Returns a JSON status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def return_count():
    """Returns the number of objects in storage by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})

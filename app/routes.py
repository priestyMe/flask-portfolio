import os
from flask import Blueprint, current_app, render_template, jsonify
from . import db  # Import db from the current package
from sqlalchemy import text  # This line should be at the top of your file

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Welcome to the Flask Portfolio App!")

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/test_connection')
def test_connection():
    try:
        # Attempt to execute a simple query
        result = db.session.execute(text("SELECT 1"))
        return jsonify(message="Connection to Azure SQL Database successful!"), 200
    except Exception as e:
        return jsonify(message=f"Connection failed: {str(e)}"), 500
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a database instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Initialize the app with the database
    db.init_app(app)

    # Import and register the Blueprint here to avoid circular import
    from app.routes import main  # Import after app is created
    app.register_blueprint(main)

    return app
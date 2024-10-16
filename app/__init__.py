import os
from flask import Flask
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Create a database instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    load_dotenv()  # Load environment variables from .env file

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@ptfoliodemoserver.database.windows.net:1433/ptfdatabase?driver=ODBC+Driver+17+for+SQL+Server'

    # Initialize the app with the database
    db.init_app(app)

    # Import and register the Blueprint here to avoid circular import
    from app.routes import main  # Import after app is created
    app.register_blueprint(main)

    return app
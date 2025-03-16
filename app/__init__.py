"""
__init__.py

Initializes the Flask app, SocketIo, and registers the routes and socket handlers.

"""

from flask import Flask
from flask_socketio import SocketIO

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Use a secure secret in production

# Initialize SocketIO with the Flask app
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for testing; restrict in production

# Import routes and socket handlers to register them with the app
from app import routes, sockets
"""
routes.py

Defines the HTTP routes for the chat application.
"""

from flask import render_template
from app import app

@app.route('/')
def index():
    """
    Render the index page which allows the user to select or create a chat room.
    """
    return render_template('index.html')

@app.route('/chat/<room>')
def chat(room):
    """
    Render the chat interface for a specific room.
    
    Args:
        room (str): The chat room name.
    """
    return render_template('chat.html', room=room)
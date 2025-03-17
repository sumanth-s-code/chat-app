"""
sockets.py

Defines SocketIO event handlers for real-time communication
"""

from flask_socketio import join_room, leave_room, emit
from app import socketio

@socketio.on('join')
def handle_join(data):
    """
    Event handler for a user joining a chat room.
    
    Args:
        data (dict): Contains 'username' and 'room' keys.
    """
    room = data.get('room')
    username = data.get('username')
    join_room(room)
    emit('status', {'msg': f'{username} has entered the room.'}, room=room)

@socketio.on('text')
def handle_text(data):
    """
    Event handler for a user sending a message.
    
    Args:
        data (dict): Contains 'username', 'room', and 'message' keys.
    """
    room = data.get('room')
    username = data.get('username')
    message = data.get('message')
    emit('message', {'msg': f'{username}: {message}'}, room=room)

@socketio.on('leave')
def handle_leave(data):
    """
    Event handler for a user leaving a chat room.
    
    Args:
        data (dict): Contains 'username' and 'room' keys.
    """
    room = data.get('room')
    username = data.get('username')
    leave_room(room)
    emit('status', {'msg': f'{username} has left the room.'}, room=room)
"""
run.py

Entry point for the chat application.
"""

from app import app, socketio

if __name__ == '__main__':
    # Run the application with SocketIO support
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
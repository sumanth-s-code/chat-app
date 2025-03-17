"""
test_sockets.py

Unit test for SocketIO events.
"""

import unittest
from flask_socketio import SocketIOTestClient
from app import app, socketio

class SocketsTestCase(unittest.TestCase):
    def setUp(self):
        # Create a SocketIO test client for the Flask app
        self.client = socketio.test_client(app)
    
    def test_join_event(self):
        """
        Test that a user joining a room triggers a status message.
        """
        data = {'username': 'testuser', 'room': 'testroom'}
        self.client.emit('join', data)
        received = self.client.get_received()
        self.assertTrue(any('status' in packet['name'] for packet in received))
    
    def test_text_event(self):
        """
        Test that sending a text message results in a broadcasted message.
        """
        data = {'username': 'testuser', 'room': 'testroom', 'message': 'Hello, world!'}
        self.client.emit('text', data)
        received = self.client.get_received()
        self.assertTrue(any('message' in packet['name'] for packet in received))
    
    def test_leave_event(self):
        """
        Test that leaving a room triggers a status message.
        """
        data = {'username': 'testuser', 'room': 'testroom'}
        self.client.emit('leave', data)
        received = self.client.get_received()
        self.assertTrue(any('status' in packet['name'] for packet in received))

if __name__ == '__main__':
    unittest.main()
"""
test_routes.py

Unit tests for the Flask HTTP routes.
"""

import unittest
from app import app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        """
        Test the index route returns a 200 status code and contains expected content.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Chat Application', response.data)

    def test_chat_route(self):
        """
        Test the chat route for a specific room returns a 200 status code and displays the room name.
        """
        room = 'testroom'
        response = self.app.get(f'/chat/{room}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes(f'Chat Room: {room}', 'utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
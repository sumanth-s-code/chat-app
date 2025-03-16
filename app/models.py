"""
models.py

Defines data models for the chat application.

For this simple example, we are using in-memory storage.

In production, consider using a database to store messages and user data.
"""

class Message:
    """
    A simple Message class to represent a chat message.
    """
    def __init__(self, username, text, room):
        """
        Initialize a Message instance.
        
        Args:
            username (str): The username of the sender.
            text (str): The text of the message.
            room (str): The chat room the message belongs to.
        """
        self.username = username
        self.text = text
        self.room = room

    def to_dict(self):
        """
        Convert the Message instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the message.
        """
        return {
            'username': self.username,
            'text': self.text,
            'room': self.room
        }
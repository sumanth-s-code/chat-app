# Real-Time Chat Application

## Overview
This project is a web-based chat application built with Flask and Flask-SocketIO that supports real-time messaging and multi-room chat functionality. Users can join a chat room, send messages, and leave the room with updates reflected in real time.

## Features
- **Multi-Room Chat:** Users can join different chat rooms.
- **Real-Time Communication:** Instant message delivery using WebSocket technology.
- **Responsive UI:** HTML templates render a dynamic chat interface.
- **Modular Structure:** Separate modules for HTTP routes, SocketIO events, and data models.
- **Unit Testing:** Unit tests for routes and socket events using Python's `unittest`.
- **Dockerization:** Containerize the application using a Dockerfile.

## Project Structure

chat_app/
├── app/
│   ├── __init__.py      # Initializes the Flask app and SocketIO
│   ├── routes.py        # HTTP route definitions
│   ├── sockets.py       # SocketIO event handlers
│   └── models.py        # Data models (in-memory example)
├── templates/
│   ├── base.html        # Base HTML template
│   ├── index.html       # Landing page for joining chat rooms
│   └── chat.html        # Chat room interface
├── tests/
│   ├── test_routes.py   # Unit tests for Flask routes
│   └── test_sockets.py  # Unit tests for SocketIO events
├── requirements.txt     # Python dependencies
├── Dockerfile           # Containerization instructions
├── README.md            # Project overview and setup instructions
└── run.py               # Entry point to run the application

## Setup and Installation

1. **Clone the repository:**

   git clone <repository_url>
   cd chat_app

2. **Using a Python Virtual Environment:**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

3. **Running the Application:**

python run.py

The application will be accessible at http://localhost:5000.

4. **Running Tests:**

python -m unittest discover tests

5. **Using Docker:**

Build the Docker image:
docker build -t chat_app .

Run the Docker container:
docker run -p 5000:5000 chat_app

The application will be accessible at http://localhost:5000.
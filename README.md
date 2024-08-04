
# WebSocket FastAPI PoC

This repository contains a proof of concept (PoC) for implementing WebSockets using FastAPI. The project demonstrates how to set up a WebSocket server with FastAPI and handle real-time communication with connected clients.

## Features

- Establish WebSocket connections with clients.
- Broadcast messages to all connected clients.
- Handle individual client connections and disconnections.
- Simple and extensible codebase for quick experimentation.

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/chandandanjo/websocket-fastapi-poc.git
cd websocket-fastapi-poc
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the FastAPI server with Uvicorn:

```bash
fastapi run server.py
```

2. Open your browser and navigate to `http://localhost:8000` to see the application in action.

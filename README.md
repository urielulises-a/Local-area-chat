# Chat Project with Server and Client using PyQt5 and Socket

This project implements a simple chat system between a server and multiple clients using sockets and the PyQt5 library for the client's graphical interface.

## Features

- Real-time communication between clients and server.
- Intuitive graphical interface for the client with options for entering a username and messages.
- Concurrent connection handling via threads on the server.

## Requirements

- Python 3.x
- PyQt5

## Project Structure

- **servidor.py**: Server code to manage client connections and forward messages.
- **cliente.py**: Chat client implementation with a graphical interface using PyQt5.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_project.git

2. Install dependencies
   ```bash
   pip install PyQt5

## Usage

1. Start server:
   ```bash
   python servidor.py
   
2. Execute client:
      ```bash
   python cliente.py
      
The client's graphical interface will open. Enter your username, type messages, and press "Send" to send them to the server and other connected clients.

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation
import socket
import threading
import sys

class ChatClient(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Chat Client")
        self.setGeometry(100, 100, 600, 400)

        # Create layout
        self.layout = QVBoxLayout(self)

        # Create chat display
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 12pt;
                margin-bottom: 10px;
            }
        """)
        self.layout.addWidget(self.chat_display)
# Create username entry
        self.username_entry = QLineEdit(self)
        self.username_entry.setPlaceholderText("Enter your name")
        self.layout.addWidget(self.username_entry)
        self.username_entry.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 12pt;
                margin-bottom: 10px;
            }
        """)
        # Create message entry
        self.message_entry = QLineEdit(self)
        self.message_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.message_entry.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 12pt;
                margin-bottom: 10px;
            }
        """)
        self.layout.addWidget(self.message_entry)
        self.message_entry.returnPressed.connect(self.send_message)
        

        # Create send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
        """)
        self.layout.addWidget(self.send_button)

        # Connect send button to send_message function
        self.send_button.clicked.connect(self.send_message)

        # Configuración del cliente
        self.server_address = ('127.0.0.1', 5555)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

        # Hilo para recibir mensajes del servidor
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self):
        username = self.username_entry.text()
        message = self.message_entry.text()
        if username and message:
            full_message = f"{username}: {message}"
            self.client_socket.send(full_message.encode('utf-8'))
            self.chat_display.append(f"<b>{username}:</b> {message}")
            self.message_entry.clear()
        else:
            self.shake_animation.start()
    def animate_message_sent(self, message):
        animation = QPropertyAnimation(self.chat_display.viewport(), b"geometry")
        animation.setDuration(300)
        animation.setStartValue(self.chat_display.viewport().geometry())
        animation.setEndValue(self.chat_display.viewport().geometry().translated(0, 30))
        animation.start()
        self.chat_display.append(f"<b>You:</b> {message}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_display.append(message)
            except ConnectionAbortedError:
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)

    chat_client = ChatClient()
    chat_client.show()

    sys.exit(app.exec_())

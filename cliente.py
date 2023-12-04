import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")

        # Área de texto para mostrar el chat
        self.chat_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_display.pack(padx=10, pady=10)

        # Entrada de texto para escribir mensajes
        self.message_entry = tk.Entry(master, width=30)
        self.message_entry.pack(padx=10, pady=10)

        # Botón para enviar mensajes
        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.pack(pady=10)

        # Configuración del cliente
        self.server_address = ('127.0.0.1', 5555)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

        # Hilo para recibir mensajes del servidor
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def receive_messages(self): 
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_display.insert(tk.END, f"{message}\n")
            except ConnectionAbortedError:
                break

# Crear la aplicación
root = tk.Tk()
app = ChatClient(root)

# Ejecutar la aplicación
root.mainloop()

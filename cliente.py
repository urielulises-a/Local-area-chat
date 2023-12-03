import socket
import threading

def recibir_mensajes(socket_cliente):
    while True:
        try:
            mensaje = socket_cliente.recv(1024)
            print(f"Mensaje recibido: {mensaje.decode('utf-8')}")
        except Exception as e:
            print(f"Error al recibir mensaje: {str(e)}")
            break

def enviar_mensajes(socket_cliente):
    while True:
        mensaje = input("Ingrese un mensaje: ")
        socket_cliente.send(mensaje.encode('utf-8'))

def iniciar_cliente():
    host = '127.0.0.1'
    port = 5555

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(cliente,))

    hilo_recibir.start()
    hilo_enviar.start()

if __name__ == "__main__":
    iniciar_cliente()

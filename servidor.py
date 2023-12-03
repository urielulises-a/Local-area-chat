import socket
import threading

def manejar_cliente(cliente, direccion, clientes_conectados):
    try:
        while True:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break
            mensaje_decodificado = mensaje.decode('utf-8')
            print(f"Mensaje de {direccion}: {mensaje_decodificado}")

            # Reenviar el mensaje a todos los clientes conectados
            for cliente_conectado in clientes_conectados:
                if cliente_conectado != cliente:
                    try:
                        cliente_conectado.send(mensaje)
                    except:
                        # Si hay un error al enviar, asumimos que el cliente se desconectó
                        clientes_conectados.remove(cliente_conectado)
    except Exception as e:
        print(f"Error en la conexión con {direccion}: {str(e)}")
    finally:
        clientes_conectados.remove(cliente)
        cliente.close()
    
def iniciar_servidor():
    host = '127.0.0.1'
    port = 5555

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen()

    print(f"Servidor escuchando en {host}:{port}")

    clientes_conectados = []

    while True:
        cliente, direccion = servidor.accept()
        print(f"Conexión aceptada de {direccion}")

        clientes_conectados.append(cliente)

        cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente, direccion, clientes_conectados))
        cliente_thread.start()

if __name__ == "__main__":
    iniciar_servidor()

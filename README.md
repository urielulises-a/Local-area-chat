# Proyecto de Chat con Servidor y Cliente usando PyQt5 y Socket

Este proyecto implementa un simple sistema de chat entre un servidor y múltiples clientes utilizando sockets y la biblioteca PyQt5 para la interfaz gráfica del cliente.

## Características

- Comunicación en tiempo real entre clientes y servidor.
- Interfaz gráfica intuitiva para el cliente con opciones de ingreso de nombre de usuario y mensajes.
- Manejo de conexiones concurrentes mediante hilos en el servidor.

## Requisitos

- Python 3.x
- PyQt5

## Estructura del Proyecto

- **servidor.py**: Código del servidor para gestionar las conexiones de los clientes y reenviar mensajes.
- **cliente.py**: Implementación del cliente de chat con interfaz gráfica utilizando PyQt5.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git

2. Instala dependencias
   ```bash
   pip install PyQt5

## Uso

1. Ejectuar servidor:
   ```bash
   python servidor.py
   
2. Ejecutar cliente:
      ```bash
   python cliente.py
      
Se abrirá la interfaz gráfica del cliente. Ingresa tu nombre de usuario, escribe mensajes y presiona "Send" para enviarlos al servidor y a otros clientes conectados.

## Contribuciones
Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, por favor, abre un problema o envía una solicitud de extracción.

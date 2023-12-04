# chat

Proyecto de Chat con Servidor y Cliente usando PyQt5 y Socket
Este proyecto implementa un simple sistema de chat entre un servidor y múltiples clientes utilizando sockets y la biblioteca PyQt5 para la interfaz gráfica del cliente.

Requisitos
Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el código:

bash

pip install PyQt5

Estructura del Proyecto
servidor.py: Contiene el código del servidor que gestiona las conexiones de los clientes y reenvía los mensajes a todos los clientes conectados.

cliente.py: Incluye la implementación del cliente de chat con una interfaz gráfica utilizando PyQt5.

Uso
Ejecutar el servidor:

bash
  python servidor.py
  El servidor comenzará a escuchar conexiones en 127.0.0.1:5555.

Ejecutar el cliente:

bash
  python cliente.py
  Se abrirá la interfaz gráfica del cliente. Ingresa tu nombre de usuario, escribe mensajes y presiona "Send" para enviarlos al servidor y a otros clientes conectados.

Notas
El código utiliza hilos para manejar múltiples conexiones simultáneas en el servidor.
La interfaz gráfica del cliente se creó con PyQt5 y permite ingresar un nombre de usuario, enviar mensajes y visualizar el historial de conversación.
Asegúrate de tener permisos suficientes para ejecutar sockets y abrir puertos en tu sistema.
Este es un proyecto básico y puede ser expandido con características adicionales como autenticación de usuarios, salas de chat, etc.
¡Diviértete chateando!

Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, por favor, abre un problema o envía una solicitud de extracción.

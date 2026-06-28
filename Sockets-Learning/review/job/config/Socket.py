import socket
import os
from dotenv import load_dotenv

load_dotenv()

IP = os.getenv('IP')
PORT = int(os.getenv('PORT'))

class Socket:
    """Clase con metodos estaticos para manejo de sockets TCP/IP."""

    @staticmethod
    def socketServer(listen_capacity):
        """Crea y retorna un socket servidor enlazado y en escucha."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((IP, PORT))
            sock.listen(listen_capacity)
            return sock
        except socket.error as e:
            raise RuntimeError(f"Error al crear el servidor: {e}")

    @staticmethod
    def socketAccept(server_socket):
        """Acepta una conexion entrante y retorna (cliente_socket, direccion)."""
        try:
            conn, addr = server_socket.accept()
            return conn, addr
        except socket.error as e:
            raise RuntimeError(f"Error al aceptar conexion: {e}")

    @staticmethod
    def socketClient():
        """Crea y retorna un socket cliente conectado al servidor."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((IP, PORT))
            return sock
        except socket.error as e:
            raise RuntimeError(f"Error al conectar al servidor: {e}")

    @staticmethod
    def msgSend(sock, message):
        """Envia un mensaje a traves del socket (codificado en utf-8)."""
        try:
            sock.send(message.encode("utf-8"))
        except socket.error as e:
            raise RuntimeError(f"Error al enviar mensaje: {e}")

    @staticmethod
    def msgRcv(sock):
        """Recibe un mensaje del socket (decodificado en utf-8)."""
        try:
            data = sock.recv(1024)
            return data.decode("utf-8")
        except socket.error as e:
            raise RuntimeError(f"Error al recibir mensaje: {e}")
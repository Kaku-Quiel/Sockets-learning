from ctypes.wintypes import POINT
import socket
from dotenv import load_dotenv
import os

load_dotenv()

IP = os.getenv('IP')
PORT = int(os.getenv('PORT'))

class Socket:
    @staticmethod
    def socketServer(listen_capacity):
        pythonSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pythonSocket.bind((IP, PORT))
        pythonSocket.listen(listen_capacity)
        return pythonSocket
    
    @staticmethod
    def socketAccept(socketServer): # Retorn a request sockets and direction 
        conn, dir = socketServer.accept()
        return conn, dir

    @staticmethod
    def socketClient():
        pythonSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pythonSocket.connect((IP, PORT))
        return pythonSocket
    
    @staticmethod
    def msgSend(_socket_, message):
        _socket_.send(message.encode("utf-8"))

    @staticmethod
    def msgRcv(_socket_):
        rcv = _socket_.recv(1024)
        return rcv.decode("utf-8")
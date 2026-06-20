import socket
import json

class Socket:
    @staticmethod
    def socketServer():
        pythonSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pythonSocket.bind(("127.0.0.1", 5000))
        return pythonSocket
    
    @staticmethod
    def socketAccept(socketServer):
        conn, dir = socketServer.accept()
        return conn, dir

    @staticmethod
    def socketClient():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    @staticmethod
    def msgSend(_socket_, message):
        _socket_.send(message.encode("utf-8"))

    @staticmethod
    def msgRcv(_socket_):
        rcv = _socket_.recv(1024)
        return rcv.decode("utf-8")
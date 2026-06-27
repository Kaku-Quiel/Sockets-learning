""" ============== Devolverse una ruta atras para poder importar Socket.py ==================== """

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

""" =========================================================================================== """

from config.Socket import Socket, IP, PORT


socket_server = Socket.socketServer(1)

def server():
    print("="*50)
    print("Server Prendido")
    print(f"Escuchando en: {IP}: {PORT}")
    print("="*50, end="\n\n")

    socket_client, dir = Socket.socketAccept(socket_server)
    print(f"Client connected: {dir}")
    print("="*50, end="\n\n")

    while True:
        cmd = Socket.msgRcv(socket_client)

        print(f"input: {cmd}")
        
        output = f"Eco: {cmd}"
        print(f"output: {output}")

        Socket.msgSend(socket_client, f"Eco: {cmd}")

        if cmd.lower() == "exit":
            socket_client.close()
            socket_server.close()
            print("Exit success...")
            break



server()
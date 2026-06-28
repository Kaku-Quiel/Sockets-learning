""" ============== Devolverse una ruta atras para poder importar Socket.py ==================== """

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

""" =========================================================================================== """

from config.Socket import Socket, IP, PORT


socket_client = Socket.socketClient()

def main():
    print("="*50)
    print("Bienvenido cliente")
    print(f"Estas conectado al: {IP}: {PORT}")
    print("="*50, end="\n\n")


    while True:
        cmd = input("cliente$: ")

        Socket.msgSend(socket_client, cmd)
        response = Socket.msgRcv(socket_client)

        if response == "exit":
            socket_client.close()
            print("Exit success...")
            break

        print(f"{response}")

main()
""" ============== Devolverse una ruta atras para poder importar Socket.py ==================== """

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

""" =========================================================================================== """

from Socket import Socket

IP = "127.0.0.1"
PORT = 7000

socket_client = Socket.socketClient()
# socket_client.connect((IP, PORT))

def main():
    print("="*50)
    print("Bienvenido cliente")
    print(f"Estas conectado al: {IP}: {PORT}")
    print("="*50, end="\n\n")


    while True:
        cmd = input("cliente$: ")

        if cmd == "exit":
            print("Exit success...")
            break

        respuesta = "error"
        error = "tipo de error"
        if respuesta == "error":
            print(f"Error: {error}")

main()
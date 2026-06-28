""" ============== Devolverse una ruta atras para poder importar Socket.py ==================== """

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

""" =========================================================================================== """

from config.Socket import Socket, IP, PORT
from Commands import Commands


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

        cmd = Socket.msgRcv(socket_client).split()

        if len(cmd) > 2:
            output = "Error: too many parameters"
            Socket.msgSend(socket_client, output)
            print(f"output: {output}")
            continue

        rcv = {
            "cmd": cmd[0],
            "parameter": cmd[1] if len(cmd) == 2 else "None"
        }

        if rcv["parameter"] != "None":
            print(f"input: {rcv['cmd']} {rcv['parameter']}")
        else:
            print(f"input: {rcv['cmd']}")

        if rcv["cmd"] not in Commands.command_list():
            output = "Error: command not found, type 'help' for commando list"
            Socket.msgSend(socket_client, output)
            print(f"output: {output}")
            continue

        cmd_result = Commands.executeCMD(rcv["cmd"], rcv["parameter"])

        if cmd_result["status"] != "success":
            output = cmd_result["value"]
            Socket.msgSend(socket_client, output)
            print(f"output: {output}")
            continue

        output = cmd_result["value"]
        print(f"output: {output}")


        Socket.msgSend(socket_client, output)

        if output == "exit":
            socket_client.close()
            socket_server.close()
            print("Exit success...")
            break

server()
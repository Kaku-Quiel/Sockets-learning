from Socket import Socket
import json

cliente_socket = Socket.socketClient()
cliente_socket.connect(("127.0.0.1", 5000)) # INTENTA CONECTARSE A DESDE LOCALHOST EN EL PUERTO 5000

cliente = {
    "nombre" : "Jeremy",
    "id" : 1,
    "estado": True,
    "mensaje": ""
}

while True:
    mss = input("Mensaje: ")
    cliente["mensaje"] = mss
    cliente_string = json.dumps(cliente)

    Socket.msgSend(cliente_socket, cliente_string)

    mensaje = Socket.msgRcv(cliente_socket)

    print(f"Mensaje del server: \n{mensaje}")

    # cliente_socket.close()
    # print("Se cerro la conexino del cliente")
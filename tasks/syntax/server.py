from Socket import Socket
import json

server_socket = Socket.socketServer("0.0.0.0", 5000)
server_socket.listen(10) # CAPACIDAD DE CLIENTES EN COLA (deja en espera la entrada de clientes)

print(f"Server en espera en {"0.0.0.0"}:{5000}")
cliente_socket, direction = Socket.socketAccept(server_socket)

while True:
    message = Socket.msgRcv(cliente_socket)
    json_cliente = json.loads(message)

    print(f"Dato ingresado de: {json_cliente["nombre"]}")
    print(f"Mensaje: {json_cliente["mensaje"]}")

    eco = f"Nombre: {json_cliente["nombre"]} \nID: {json_cliente["id"]} \nEstado: {json_cliente["estado"]}"
    Socket.msgSend(cliente_socket, eco)

    # CERRAR LAS CONEXIONES
    # cliente.close()
    # server_socket.close()
    # print("Se cerro la conexion del server")
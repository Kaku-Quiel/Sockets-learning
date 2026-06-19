import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CREACION DEL SOCKET
server_socket.bind(('0.0.0.0', 5000)) # ASIGNARLE UN HOST Y PORT AL SOCKET DEL SERVER (desde donde le llegaran señales, (EL PUERTO MAYOR A 1024))
server_socket.listen(10) # CAPACIDAD DE CLIENTES EN COLA (deja en espera la entrada de clientes)

print(f"Server en espera en {"0.0.0.0"}:{5000}")


conexion, direccion = server_socket.accept() # ACEPTA LA CONEXION ENTRANTE Y GUARDA LOS DATOS DEL CLIENTE EN UNA TUPLA CON (conexion, direccion)

print(f"Cliente se conecto: ({conexion}, {direccion})")

mensaje = "Hola nuevo cliente, el server te da la bienvenida"
conexion.send(mensaje.encode("utf-8"))


# CERRAR LAS CONEXIONES
conexion.close()
server_socket.close()
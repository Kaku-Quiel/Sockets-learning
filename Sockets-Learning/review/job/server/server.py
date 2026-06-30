# Ajuste de path para importar modulos desde la raiz
from asyncio import as_completed
import sys
import os
from urllib import response
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.Socket import Socket, IP, PORT
from Commands import Commands
from config.Archives import Archives

def manejar_cliente(socket_cliente, direccion):
    """Maneja la comunicacion con un cliente conectado."""
    print(f"Cliente conectado: {direccion}")
    print("="*50, end="\n\n")

    while True:
        try:
            mensaje = Socket.msgRcv(socket_cliente)
            if not mensaje:  # Cliente cerro la conexion
                print("Cliente desconectado.")
                break

            partes = mensaje.split()
            if len(partes) > 2:
                output = "Error: Demasiados parametros"
                Socket.msgSend(socket_cliente, output)
                print(f"salida: {output}")
                continue

            cmd = partes[0]
            param = partes[1] if len(partes) == 2 else "None"

            # Mostrar entrada
            if param != "None":
                print(f"entrada: {cmd} {param}")
            else:
                print(f"entrada: {cmd}")

            # Validar comando
            if cmd not in Commands.command_list():
                output = "Error: comando no encontrado, escriba 'help' para lista"
                Socket.msgSend(socket_cliente, output)
                print(f"salida: {output}")
                continue
            
            """ =========== EXECUTE CMD =========== """
            resultado = Commands.executeCMD(cmd, param)
            """ =================================== """

            output = resultado["value"]
            
            if resultado["status"] != "success":
                print(f"salida: {output}")
                Socket.msgSend(socket_cliente, output)
                continue

            if output[:len("error")].lower() == "error":
                print(f"salida: {output}")
                Socket.msgSend(socket_cliente, output)
                continue

            if output == "exit":
                Socket.msgSend(socket_cliente, output)
                break

            if cmd == "descargar":
                weight_separate = output.split("||")
                weight_file = weight_separate[0]
                weight_transfer = weight_separate[1]
                
                output = f"Descargar: {weight_file} bytes\nTransferir: {weight_transfer} bytes"
                print(f"salida:\n{output}")

                Socket.msgSend(socket_cliente, output)
                respuesta = Socket.msgRcv(socket_cliente)

                print(f"entrada: {respuesta}")
                
                if respuesta == "n" or respuesta != "s":
                    Socket.msgSend(socket_cliente, "cancel")
                    print("salida: cancel")
                    continue

                Socket.msgSend(socket_cliente, "continue")
                print("salida: continue",end="\n\n")

                while True:
                    str_i = Socket.msgRcv(socket_cliente)
                    i = int(str_i) + 1
                    Socket.msgSend(socket_cliente, str(i))
                    print(f"Mandando archivo: {i}")
                    
                    if i >= 99999:
                        print("finish")
                        break

                continue

            print(f"salida: {output}")
            Socket.msgSend(socket_cliente, output)

        except (ConnectionResetError, BrokenPipeError, RuntimeError) as e:
            print(f"Error de comunicacion con el cliente: {e}")
            break

    try:
        socket_cliente.close()
    except:
        pass
    print("Conexion cerrada.")


def servidor():
    """Inicia el servidor y acepta una unica conexion (como en el original)."""
    print("="*50)
    print("Servidor encendido")
    print(f"Escuchando en: {IP}:{PORT}")
    print("="*50, end="\n\n")

    server_socket = Socket.socketServer(1)
    try:
        cliente_socket, direccion = Socket.socketAccept(server_socket)
        manejar_cliente(cliente_socket, direccion)
    except RuntimeError as e:
        print(f"Error en el servidor: {e}")
    finally:
        try:
            server_socket.close()
        except:
            pass
        print("Servidor finalizado.")


if __name__ == "__main__":
    servidor()
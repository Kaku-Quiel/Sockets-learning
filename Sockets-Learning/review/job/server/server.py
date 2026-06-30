# Ajuste de path para importar modulos desde la raiz
import sys
import os
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
            

            resultado = Commands.executeCMD(cmd, param)
            output = resultado["value"]
            
            if cmd == "descargar":
                print("bloques:\n")
                

                lista_data_block = output.split("||")
                for i in range(len(lista_data_block) - 1):
                    Archives.printDataBlock(lista_data_block[i])
                
                print(f"Bytes: {len(output)}")
                
                output = f"descargar{output}"

            else:
                print(f"salida: {output}")

            Socket.msgSend(socket_cliente, output)

            # Si hubo error, saltamos el resto del bucle (incluyendo la comprobación de 'exit')
            if resultado["status"] != "success":
                continue

            # Si el comando fue 'exit', cerramos la conexión
            if output == "exit":
                break

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
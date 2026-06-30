# Ajuste de path para importar modulos desde la raiz
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.Socket import Socket, IP, PORT
from Function import Function
from config.Archives import Archives

def main():
    """Bucle principal del cliente."""
    print("="*50)
    print("Bienvenido cliente")
    print(f"Conectado a: {IP}:{PORT}")
    print("="*50, end="\n\n")

    try:
        socket_cliente = Socket.socketClient()
    except RuntimeError as e:
        print(f"Error de conexion: {e}")
        return

    while True:
        try:
            entrada = input("cliente$: ").rstrip()
            if not entrada:
                continue

            Socket.msgSend(socket_cliente, entrada)
            respuesta = Socket.msgRcv(socket_cliente)

            if respuesta == "exit":
                break

            elif respuesta == "listar-c":
                print(Function.listar_c())
                continue

            elif respuesta[:len("Descargar")] == "Descargar":
                print(respuesta)

                posible_response = ['s', 'n']
                while True:
                    descargar = input("Descargar (S/n): ").lower()

                    if descargar in posible_response:
                        Socket.msgSend(socket_cliente, descargar)
                        break

                    print("Escriba la letra 'S' para descargar o la 'N' para no descargar")

                respuesta = Socket.msgRcv(socket_cliente)

                if respuesta == "cancel" or respuesta != "continue":
                    continue
                
                print("Descargando...",end="\n\n")

                i = 0
                while True:
                    Socket.msgSend(socket_cliente, str(i))
                    str_i = Socket.msgRcv(socket_cliente)
                    i = int(str_i)

                    print(f"descargando archivo: {i}")

                    if i >= 99999:
                        print(f"finish")
                        break
                    


            else:
                print(respuesta)

        except (KeyboardInterrupt, EOFError):
            print("\nCerrando cliente...")
            break
        except RuntimeError as e:
            print(f"Error de comunicacion: {e}")
            break

    try:
        socket_cliente.close()
    except:
        pass
    print("Cliente finalizado.")


if __name__ == "__main__":
    main()
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

            if respuesta == "info-c":
                print(Function.info())
                continue

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
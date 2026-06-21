import sys
import os

# Obtener la ruta absoluta del directorio raíz
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

from config.Socket import Socket
from Operators import Operators

server = Socket.socketServer()
server.listen(1) # CAPACIDAD DE CLIENTES EN COLA (deja en espera la entrada de clientes)

print(f"Server en espera en {"127.0.0.1"}:{5000}")
cliente, direction = Socket.socketAccept(server)

while True:
    message = Socket.msgRcv(cliente)
    operation = message.split()
    

    if message.lower() == "salir":
        server.close()
        cliente.close()
        print(f"Saliendo...")
        break
    
    if len(operation) != 3:
        print(f"Error: Operacion no valida, solo dos parametros porfavor")
        continue


    num1, operator, num2 = operation
    print(f"data in: {operation}")

    try:
        num1 = float(num1)
        num2 = float(num2)

        resultado = Operators.doMath(num1, num2, operator)

        Socket.msgSend(cliente, f"{resultado}")
        print(f"data out: {resultado}")

    except Exception as e:
        Socket.msgSend(cliente, f"Error: {e}")
        print(f"data out: Error: {e}")
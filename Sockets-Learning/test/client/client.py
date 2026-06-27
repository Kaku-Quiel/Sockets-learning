import sys
import os

# Obtener la ruta absoluta del directorio raíz
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import subprocess
from config.Socket import Socket
from Validate import Validate

subprocess.run(["clear"])

cliente = Socket.socketClient()
cliente.connect(("127.0.0.1", 5000))


while True:
    operacion = input(f"Ingrese una operacion: ")

    if operacion.lower() == "salir":
        Socket.msgSend(cliente, operacion)
        cliente.close()
        print(f"Saliendo del programa")
        break
    
    data = Validate.isValid(operacion)

    if not data["codigo"]:
        print(f"{data["message"]}\n")

    else:
        Socket.msgSend(cliente, operacion)

        resultado = Socket.msgRcv(cliente);
        print(f"Resultado: {resultado}\n")
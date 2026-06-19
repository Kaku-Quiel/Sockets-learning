import socket

# Configuración
HOST = '127.0.0.1'    # localhost = solo conexiones de esta máquina
PORT = 5000         # Puerto (elegir uno mayor a 1024 para evitar permisos)

# Crear socket servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)  # Máximo 1 cliente en cola de espera

print(f"🚀 Servidor escuchando en {HOST}:{PORT}...")
print("⏳ Esperando que un cliente se conecte...\n")

# Aceptar conexión entrante
conexion, direccion = servidor.accept()
print(f"✅ ¡Cliente conectado desde {direccion}!")

# Enviar mensaje de bienvenida
mensaje = "¡Hola, cliente! Bienvenido al servidor 🎉\n"
conexion.send(mensaje.encode('utf-8'))  # Convertir string a bytes, y mandarlo con formato compatible

print("📤 Mensaje enviado. Cerrando conexión...")
conexion.close()
servidor.close()
print("🔒 Servidor cerrado.")
import socket

HOST = '127.0.0.1'  # El mismo que el servidor
PORT = 5000

# Crear socket cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"🔗 Intentando conectar a {HOST}:{PORT}...")
cliente.connect((HOST, PORT)) #busca la conexion al host y port
print("✅ Conectado al servidor!\n")

# Recibir datos (buffer de 1024 bytes)
datos = cliente.recv(1024)
mensaje = datos.decode('utf-8')

print("📥 Mensaje del servidor:")
print("─" * 35)
print(mensaje)
print("─" * 35)

cliente.close()
print("🔒 Conexión cerrada.")
import socket

# Crear un socket TCP/IPv4
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el nombre del host local
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)

print(f"✅ Socket creado: {mi_socket}")
print(f"🖥️  Hostname: {hostname}")
print(f"📍 IP local: {ip_local}")
print(f"📦 Familia: IPv4 (AF_INET)")
print(f"🔗 Tipo: TCP (SOCK_STREAM)")

# Cerrar el socket
mi_socket.close()
print("🔒 Socket cerrado.")
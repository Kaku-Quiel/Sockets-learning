import hashlib
import random
import string


# === CREAR ARCHIVO ===
texto = [
    b"Habia una vez una duende que se pintaba la cara\n",
    b"ese duende comia mucho y masticaba con la boca llena\n",
    b"tenia la boca tan llena que se le podian reventar los cachetes\n",
    b"el nunca dejo de creer\n",
    b"asi que cuando termino de llenarse los cachetes\n",
    b"procede a pintarse la cara con pintura\n",
    b"todos los dias hace los mismo\n",
    b"nunca para y siempre se alegra"
]

try:
    with open("docs/blocks.txt", "xb") as archive:
        archive.writelines(texto)
    print("Archivo creado")
except FileExistsError:
    print("Archivo ya existía")

# === FUNCIONES ===
def byte_to_bits(texto_bytes):
    """Convierte bytes a string de 0s y 1s (para mostrar)"""
    bits = []
    for byte in texto_bytes:
        bits.append(format(byte, '08b'))
    return ' '.join(bits)

def hashear_bytes(datos_bytes):
    """Hashea DIRECTAMENTE los bytes (sin convertir a texto)"""
    hash_obj = hashlib.sha256(datos_bytes)
    return hash_obj.hexdigest()

def verify(bloque, hash_guardado):
    """Verifica que el hash del bloque coincida"""
    hash_calculado = hashear_bytes(bloque)
    return hash_calculado == hash_guardado

def corruptBytes(block):
    pos = random.randint(0, len(block) - 1)

    lista_bytes = list(block)

    while True:
        caracter = random.randint(0, 255)

        if caracter != lista_bytes[pos]:
            lista_bytes[pos] = caracter
            break

    return bytes(lista_bytes)


def leer_bloques(archivo, tam_bloque=50):
    """Lee archivo en bloques y calcula hash de cada uno"""
    lista = []
    
    with open(f"docs/{archivo}", "rb") as file:
        num_block = 1
        offset = 0
        
        while True:
            bloque = file.read(tam_bloque)
            if not bloque:
                break

            hash_block = hashear_bytes(bloque)
            
            # Guardar metadata
            data_block = {
                "number": num_block,
                "hash": hash_block,
                "init_offset": offset,
                "size": len(bloque),
                "bits": byte_to_bits(bloque),  # Solo para mostrar
                "status": ""
            }

            if random.randint(1, 3) == 3:
                bloque = corruptBytes(bloque)
            
            # Verificar integridad (siempre debe ser True aquí)
            data_block["status"] = "success" if verify(bloque, data_block['hash']) else "error"

            lista.append(data_block)

            print(data_block)
            print()
            
            num_block += 1
            offset += len(bloque)
    
    return lista

# === EJECUTAR ===
print("\n" + "="*50)
print("LEYENDO ARCHIVO EN BLOQUES")
print("="*50 + "\n")

bloques = leer_bloques("blocks.txt", 50)

print("="*50)
print(f"RESULTADO FINAL")
print("="*50)
print(f"Total bloques: {len(bloques)}")
print(f"Total bytes: {sum(b['size'] for b in bloques)}")
import hashlib
import random


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

def randomCorrupt(block, probabilidad):
    if random.randint(1, probabilidad) == probabilidad:
        return {
            "block": corruptBytes(block),
            "error": True
        }
    return {
        "block": block,
        "error": False
    }

def printDataBlock(data_block):
    print(f"Bloque: {data_block['number']}")
    print(f"  Hash: {data_block['hash'][:32]}...")
    print(f"  init offset: {data_block['init_offset']}")
    print(f"  end offset: {data_block['end_offset']}")
    print(f"  size: {data_block['size']}")
    print(f"  bits: {data_block['bits']}")
    print(f"  status: {data_block['status']}")
    print()

def leer_bloques(archivo, tam_bloque=50):
    """Lee archivo en bloques y calcula hash de cada uno"""
    lista = []
    
    with open(f"docs/{archivo}", "rb+") as file:
        num_block = 1
        init_offset = 0
        end_offset = 0

        errores = 0
        intentos = 0
        i = 0

        while True:
            original_bloque = file.read(tam_bloque)
            if not original_bloque:
                break
            

            data_random = randomCorrupt(original_bloque, 2)
            bloque = data_random['block']

            hash_block = hashear_bytes(bloque)
            end_offset = end_offset + len(bloque)

            if data_random['error']:
                errores += 1

            # Guardar metadata
            
            data_block = {
                "number": num_block,
                "hash": hash_block,
                "init_offset": init_offset,
                "end_offset": end_offset - 1,
                "size": len(bloque),
                "bits": (bloque),  # Solo para mostrar
                "status": ""
            }
            
            # Verificar integridad (siempre debe ser True aquí)
            data_block["status"] = "success" if verify(original_bloque, data_block['hash']) else "error"

            lista.append(data_block)
            
            while True:
                if data_block['status'] == "error":
                    file.seek(init_offset)

                    dist = (end_offset + 1) - init_offset

                    data_random = randomCorrupt(file.read(dist), 2)
                    bloque = data_random["block"]

                    i += 1

                    if i >= 5:
                        data_block["status"] = "transmition error"
                        break

                    if not data_random["error"]:
                        data_block["hash"] = hashear_bytes(bloque)
                        data_block['bits'] = bloque
                        data_block["status"] = "fixed"

                else:
                    break
            
            intentos += i
            i = 0

            num_block += 1
            init_offset += len(bloque)
    
    return {
        "lista": lista,
        "intentos": intentos,
        "errores": errores
    }

# === EJECUTAR ===
data_lectura = leer_bloques("blocks.txt", 50)

print("\n" + "="*50)
print("LEYENDO ARCHIVO EN BLOQUES")
print("="*50 + "\n")

for data_block in data_lectura["lista"]:
    printDataBlock(data_block)


print("="*50)
print(f"RESULTADO FINAL")
print("="*50)
print(f"Total bloques: {len(data_lectura['lista'])}")
print(f"Total bytes: {sum(b['size'] for b in data_lectura['lista'])}")
print(f"Errores: {data_lectura['errores']}")
print(f"Numero de veces que se intento corregir: {data_lectura['intentos']}")
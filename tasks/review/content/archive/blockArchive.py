import hashlib
import random
import string

from cupshelpers import Printer


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

def corruptBlock(block):
    block = block.decode("utf-8")
    caracter = random.choice(string.ascii_letters + string.digits)
    pos = int(len(block) / 2)
    
    badBlock = []
    for i in range(0, len(block) - 1):

        if i == pos:
            badBlock.append(caracter)
            continue

        badBlock.append(block[i])

    return ''.join(badBlock).encode("utf-8")



def leer_bloques(archivo, tam_bloque=50):
    """Lee archivo en bloques y calcula hash de cada uno"""
    lista = []
    
    with open(f"docs/{archivo}", "rb") as file:
        num_block = 1
        offset = 0
        doIt = True
        
        while True:
            bloque = file.read(tam_bloque)
            if not bloque:
                break

            numero = random.randint(1, 3)

            hash_block = None

            if doIt and numero == 3:
                doIt = False
                badBlock = corruptBlock(bloque)
                hash_block = hashear_bytes(badBlock)
            else:                
                # Calcular hash de LOS DATOS (bytes)
                hash_block = hashear_bytes(bloque)
            
            # Guardar metadata
            data_block = {
                "number": num_block,
                "hash": hash_block,
                "init_offset": offset,
                "size": len(bloque),
                "bits": byte_to_bits(bloque)  # Solo para mostrar
            }
            
            # Verificar integridad (siempre debe ser True aquí)
            if verify(bloque, hash_block):
                print(f"Bloque {num_block}:")
                print(f" Offset: {offset}")
                print(f" Size: {len(bloque)} bytes")
                print(f" Hash: {hash_block}")
                print(f" Bits: {byte_to_bits(bloque)[:30]}...")  # Primeros 30 caracteres
                print()
                lista.append(data_block)
            else:
                print(f"   Bloque {num_block} CORRUPTO!")
            
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
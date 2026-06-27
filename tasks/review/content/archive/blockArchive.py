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
    return bits

def hashear_bytes(datos_bytes):
    """Hashea DIRECTAMENTE los bytes (sin convertir a texto)"""
    hash_obj = hashlib.sha256(datos_bytes)
    return hash_obj.hexdigest()

def verify(bloque, hash_guardado):
    """Verifica que el hash del bloque coincida"""
    hash_calculado = hashear_bytes(bloque)
    return hash_calculado == hash_guardado

def corruptBytes(lista_bits):

    block = [int(bits, 2) for bits in lista_bits]

    pos = random.randint(0, len(block) - 1)

    # lista_bytes = list(block)

    while True:
        caracter = random.randint(0, 255)

        if caracter != block[pos]:
            block[pos] = caracter
            break

    return bytes(block)

def randomCorrupt(lista_bits, probabilidad):
    block = bytes([int(bits, 2) for bits in lista_bits])

    if random.randint(1, probabilidad) != probabilidad:
        return {
            "block": block,
            "error": False
        }
    return {
        "block": corruptBytes(lista_bits),
        "error": True
    }

def printDataBlock(data_block):
    print(f"Bloque: {data_block['number']}")
    # print(f"  content: {randomCorrupt(data_block['bits'], 99999999999999999999999999)['block']}") # Ver mensaje explicito
    print(f"  Hash: {data_block['hash'][:32]}...")
    print(f"  init offset: {data_block['init_offset']}")
    # print(f"  end offset: {data_block['end_offset']}")
    print(f"  size: {data_block['size']}")
    print(f"  bits: {data_block['bits'][0]} {data_block['bits'][1]} {data_block['bits'][2]}...")
    print(f"  status: {data_block['status']}")
    print()

def resultado(titulo, data):
    print(f"\n\n")
    print(titulo, end='')
    print("="*50)
    for data_block in data['lista']:
        printDataBlock(data_block)

    print("="*50)
    print("RESULTADO FINAL")
    print("="*50)
    print(f"Num blocks: {data['num_blocks']}")
    print(f"Total Bytes: {data['bytes_total']}")
    print(f"Paso por Red: {data['red']}")

def fixDataBlock(data_block, read_size, status="success"):
    errors = 0

    with open("docs/blocks.txt", "rb+") as file:
        while True:
            if data_block['status'] == "success":
                break

            else:
                file.seek(data_block['init_offset'])
                bloque = file.read(read_size)
                hash_block = hashear_bytes(bloque)

                if verify(bloque, hash_block):
                    data_block["hash"] = hash_block
                    data_block["bits"] = byte_to_bits(bloque)
                    data_block['status'] = status
                    break

            errors += 1
            if errors < 100:
                data_block["status"] = "transmition error"
                data_block["bits"] = 0
                data_block["hash"] = "transmition error"
                break

        return data_block

def emisor(read_size = 50, mode = "normal", error_list=[], block_list=[]):
    if mode == "normal":
        lista = []

        with open("docs/blocks.txt", "rb+") as file:
            num_block = 1
            init_offset = 0

            while True:
                bloque = file.read(read_size)
                if not bloque:
                    break

                data_block = {
                    "number": num_block,
                    "hash": None,
                    "bits": None,
                    "size": len(bloque),
                    "init_offset": init_offset,
                    "status": ""
                }

                data_block = fixDataBlock(data_block, read_size)

                lista.append(data_block)
            
                num_block += 1
                init_offset += len(bloque)

        return {
            "lista": lista,
            "num_blocks": len(lista),
            "bytes_total": sum(b['size'] for b in lista),
            "red": False
        }
    
    if mode == "reply":
        lista_fixed = []

        if error_list == []:
            return {
                "lista": block_list,
                "status": "success",
                "Error": None
                }
        
        if block_list == []:
            return {
                "lista": block_list,
                "status": "error",
                "Error": "E01"
            }

        for num_block in error_list:
            data_block = block_list[num_block - 1]

            if data_block["status"] == "success":
                return {
                    "lista": block_list,
                    "status": "error",
                    "Error": "E02"
                }
            
            data_block = fixDataBlock(data_block, read_size, "fixed")

            lista_fixed.append(data_block)

        for data_block_fixed in lista_fixed:
            for data_block in block_list:
                if data_block['number'] == data_block_fixed['number']:
                    data_block = data_block_fixed
            

        return {
            "lista": block_list,
            "status": "success",
            "Error": None
        }



def red(data_emisor):
    for data_block in data_emisor['lista']:
        bits = data_block["bits"]
        
        data_random = randomCorrupt(bits, 3)

        if data_random["error"]:
            data_block['status'] = "error"
            data_block['hash'] = hashear_bytes(data_random['block'])
            data_block['bits'] = byte_to_bits(data_random["block"])

    data_emisor['red'] = True

def receptor(data_receptor):

    lista = data_receptor['lista']

    lista_errores = []

    for data_block in lista:
        if data_block['status'] != "success":
            lista_errores.append(data_block['number'])

    lista = emisor(mode="reply", error_list=lista_errores, block_list=lista) # arreglar la lista

    return data_receptor

    
        

data_emisor = emisor()

resultado("EMISOR: ", data_emisor)

red(data_emisor)

resultado("RED: ", data_emisor)

data_receptor = receptor(data_emisor)

resultado("RECEPTOR: ", data_receptor)
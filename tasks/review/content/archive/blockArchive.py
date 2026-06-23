texto = [b"Habia una vez una duende que se pintaba la cara\n", b"ese duende comia mucho y masticaba con la boca llena\n", b"tenia la boca tan llena que se le podian reventar los cachetes\n",
         b"el nunca dejo de creer\n", b"asi que cuando termino de llenarse los cachetes\n", b"procede a pintarse la cara con pintura\n", b"todos los dias hace los mismo\n",
         b"nunca para y siempre se alegra"]
try:
    with open("docs/blocks.txt", "xb") as archive:
        archive.writelines(texto)

except:
    print("Archivo ya creado")

def byte_to_bits(texto):
    bits = []
    for byte in texto:
        bits.append(format(byte, '08b'))
    return ' '.join(bits)

def leer_bloques(archivo):
    lista = []

    with open(f"docs/{archivo}", "rb") as file:
        num_block = 1
        offset = 0

        while True:
            bloque = file.read(50)

            if not bloque:
                break

            data_block = {
                "number": num_block,
                "block": byte_to_bits(bloque),
                "init_offset": offset,
                "size": len(bloque)
            }
            
            print(f"bloque {data_block['number']}: {data_block}\n")
            lista.append(data_block)

            num_block += 1
            offset += data_block["size"]

    return lista


bloques = leer_bloques("blocks.txt")
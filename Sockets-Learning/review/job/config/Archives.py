import hashlib

class Archives:
    @staticmethod
    def load_archive(archive, side):
        dir = "ERROR"
        if side == "server":
            dir = "../server/archivos_servidor"
        elif side == "client":
            dir = "../client/archivos_cliente"

        if dir == "ERROR":
            return "Error de sistema: no hay especificacion de directorio de archivo"
        
        _SIZE_READ_ = 5
        try:
            with open(f"{dir}/{archive}", "rb+") as file:
                number = 1
                offset = 0

                string_data_block = ""

                while True:
                    block = file.read(_SIZE_READ_)
                    if not block:
                        break
                    
                    hashblock = Archives._hashblock(block)
                    bitsblock = Archives._bitsblock(block, mode="neutral")
                    size = len(block)

                    string_data_block +=       "number:" + f"{number}"
                    string_data_block += "//" + "hash:"   + f"{hashblock}"
                    string_data_block += "//" + "bits:"   + f"{bitsblock}"
                    string_data_block += "//" + "offset:" + f"{offset}"
                    string_data_block += "//" + "size:"   + f"{size}"
                    string_data_block += "//" + "status:" + f"success"

                    string_data_block += "||" # Final del data_block

                    number += 1
                    offset += size

                return string_data_block
            
            return "Error archivos: como coño llegue aqui"
            
        except Exception as e:
            return f"Error archivos: {e}"
        
    @staticmethod
    def _hashblock(block):
            hashblock = hashlib.sha256(block)
            return hashblock.hexdigest()
    
    @staticmethod
    def _bitsblock(block_or_bits, mode="neutral"):
            if mode == "neutral":
                block = block_or_bits

                bits = []
                for byte in block:
                    bits.append(format(byte, '08b'))
                return " ".join(bits)
            
            if mode == "reverse":
                bits = block_or_bits
                lista_str_bytes = bits.split(bits)

                lista_int_bytes = []

                for str_byte in lista_str_bytes:
                    lista_int_bytes.append(int(str_byte, 2))

                return bytes(lista_int_bytes)
            
            return "ERROR: no se encontro un modo para la conversion"
        

    
    @staticmethod
    def _verify_hash(data_block):
        return "True"
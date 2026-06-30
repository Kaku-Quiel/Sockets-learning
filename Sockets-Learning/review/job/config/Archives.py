import hashlib
import re

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
        
        _SIZE_READ_ = 100
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
                    size = len(block)

                    string_data_block += f"{number}"
                    string_data_block += "//" + f"{hashblock}"
                    string_data_block += "//" + f"{block}"
                    string_data_block += "//" + f"{offset}"
                    string_data_block += "//" + f"{size}"
                    string_data_block += "//" + f"success"

                    string_data_block += "||" # Final del data_block

                    number += 1
                    offset += size

                return string_data_block
            
            return "Error archivos: como coño llegue aqui"
            
        except Exception as e:
            return f"Error archivos: {e}"
        
    @staticmethod
    def request_download(archive, side):
        dir = "ERROR"
        if side == "server":
            dir = "../server/archivos_servidor"
        elif side == "client":
            dir = "../client/archivos_cliente"

        if dir == "ERROR":
            return "Error de sistema: no hay especificacion de directorio de archivo"
        
        _SIZE_READ_ = 1024
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
                    size = len(block)

                    string_data_block += f"{number}"
                    string_data_block += "//" + f"{hashblock}"
                    string_data_block += "//" + f"{block}"
                    string_data_block += "//" + f"{offset}"
                    string_data_block += "//" + f"{size}"
                    string_data_block += "//" + f"success"

                    string_data_block += "||" # Final del data_block

                    number += 1
                    offset += size

                file.seek(0)
                weight_file = len(file.read())
                weight_transfer = len(string_data_block)

                return f"{weight_file}||{weight_transfer}"

            return "Error request: como coño llegue aqui"
        except Exception as e:
            return f"Error request: {e}"
        
    @staticmethod
    def _hashblock(block):
            hashblock = hashlib.sha256(block)
            return hashblock.hexdigest()
    
    @staticmethod
    def _verify_hash(string_data_block):
        separate_data_block = string_data_block.split("//")

        hashblock = separate_data_block[1]
        block = separate_data_block[2]

        return hashblock == Archives._hashblock(block)
    
    @staticmethod
    def printDataBlock(data_block):
        json_block = data_block.split("//")

        number = json_block[0]
        hash = json_block[1]
        bits = json_block[2]
        offset = json_block[3]
        size = json_block[4]
        status = json_block[5]

        string_data_block = f"Block: {number}\n"
        string_data_block += f"  Hash: {hash[:15]}...\n"
        string_data_block += f"  Bits: {bits[:15]}...\n"
        string_data_block += f"  Offset: {offset}\n"
        string_data_block += f"  Size: {size}\n"
        string_data_block += f"  status: {status}\n"

        print(string_data_block)

from pathlib import Path


commands = (
    "help",
    "exit",
    "info",
    "info-c",
    "subir",
    "descargar"
)

""" ============================== CLASS ============================== """

class Commands:

    @staticmethod
    def command_list():
        cmd_list = []

        for i in range(len(commands)):
            cmd_list.append(commands[i])

        return cmd_list

    @staticmethod
    def executeCMD(cmd, parameter):
        cmd_result = {
            "status": "error",
            "value": "Error: Command not found"
        }
        if cmd not in commands:
            return cmd_result
        
        cmd_result["status"] = "success"
                
        if cmd == "exit":
            cmd_result["value"] = exit(parameter)
            return cmd_result
        
        elif cmd == "help":
            cmd_result["value"] = helpCMD(parameter)
            return cmd_result
        
        elif cmd == "subir":
            cmd_result["value"] = subirCMD(parameter)
            return cmd_result
        
        elif cmd == "descargar":
            cmd_result["value"] = descargarCMD(parameter)
            return cmd_result
        
        elif cmd == "info":
            cmd_result["value"] = infoCMD(parameter)
            return cmd_result
        
        elif cmd == "info-c":
            cmd_result["value"] = client_infoCMD(parameter)
            return cmd_result
        

        else:
            return {
            "status": "Fatal",
            "value": "Fatal"
        }

""" ============================ FUNCTIONS ============================ """

def exit(parameter):
    if parameter != "None":
        return "Error: Parameter not compatible"
    return "exit"

def helpCMD(parameter):
    if parameter != "None":
        return "Error: Parameter not compatible"
    
    string_command_list = "\n" + "="*50 + "\nLista de comandos\n" + "="*50 + "\n"

    for i in range(len(commands)):
        if commands[i] == "descargar" or commands[i] == "subir":
            string_command_list += f"-{commands[i]} archivo\n"
        else:
            string_command_list += f"-{commands[i]}\n"

    return string_command_list

def subirCMD(parameter):
    if parameter == "None":
        return "Error: Parameter not Found"

    return "prueba"

def descargarCMD(parameter):
    if parameter == "None":
        return "Error: Parameter not Found"

    return "prueba"

def infoCMD(parameter):
    if parameter != "None":
        return "Error: Parameter not compatible"

    string_archive_list = "\n" + "="*50 + "\nLista de archivos del servidor\n" + "="*50 + "\n"
    i = 1

    archive_list = Path("archivos_servidor").glob("*")
    for archive in archive_list:
        string_archive_list += f"{i}. {archive.name}\n"
        i += 1

    return string_archive_list

def client_infoCMD(parameter):
    if parameter != "None":
        return "Error: Parameter not compatible"
    
    return "info-c"
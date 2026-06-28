commands = (
    "help",
    "exit",
    "subir",
    "descargar"
)

class Commands:

    @staticmethod
    def command_list():
        cmd_list = []

        for i in range(len(commands)):
            cmd_list.append(commands[i])

        return cmd_list

    @staticmethod
    def executeCMD(cmd):
        cmd_result = {
            "status": "error",
            "value": "Error: Command not found"
        }
        if cmd not in commands:
            return cmd_result
        

        
        cmd_result["status"] = "success"
                
        if cmd == "exit":
            cmd_result["value"] = exitCMD()
            return cmd_result
        
        elif cmd == "help":
            cmd_result["value"] = helpCMD()
            return cmd_result
        
        elif cmd == "subir":
            cmd_result["value"] = subirCMD()
            return cmd_result
        
        elif cmd == "descargar":
            cmd_result["value"] = descargarCMD()
            return cmd_result
        

        else:
            return {
            "status": "Fatal",
            "value": "Fatal"
        }
        
        
        

    

def helpCMD():
    string_command_list = ""
    for i in range(len(commands)):
        string_command_list += f"-{commands[i]}\n"

    return string_command_list

def exitCMD():
    return "exit"

def subirCMD():
    return "prueba"

def descargarCMD():
    return "prueba"
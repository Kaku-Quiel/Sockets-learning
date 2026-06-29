import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from config.Archives import Archives

# Lista de comandos disponibles (usada para help y validacion)
COMMANDS = (
    "help",
    "exit",
    "listar",
    "listar-c",
    "subir",
    "descargar"
)

def ARCHIVE_LIST():
    server_dir = Path("archivos_servidor")

    if not server_dir.exists():
        server_dir.mkdir(parents=True, exist_ok=True)

    archives = []
    try:
        for arch in server_dir.glob("*"):
            archives.append(arch.name)
    except OSError as e:
        return f"Error al leer directorio: {e}"
    
    return archives

class Commands:
    """Clase que maneja la ejecucion de comandos del servidor."""

    @staticmethod
    def command_list():
        """Retorna la lista de comandos como tupla."""
        return COMMANDS

    @staticmethod
    def executeCMD(cmd, parameter):
        """
        Ejecuta el comando indicado con el parametro dado.
        Retorna un diccionario con {'status': 'success'|'error', 'value': ...}
        """
        # Mapeo de comandos a funciones (funciones estaticas definidas abajo)
        command_map = {
            "exit": Commands._exit,
            "help": Commands._help,
            "subir": Commands._subir,
            "descargar": Commands._descargar,
            "listar": Commands._listar,
            "listar-c": Commands._listar_c,
        }

        if cmd not in command_map:
            return {
                "status": "error",
                "value": "Error: Comando no encontrado"
            }

        try:
            result = command_map[cmd](parameter)
            return {
                "status": "success",
                "value": result
            }
        except Exception as e:
            # Captura cualquier error interno y lo retorna como error
            return {
                "status": "error",
                "value": f"Error interno: {e}"
            }

    # ---------- Funciones de comando (privadas) ----------

    @staticmethod
    def _exit(parameter):
        if parameter != "None":
            return "Error: Parametro no compatible"
        return "exit"

    @staticmethod
    def _help(parameter):
        if parameter != "None":
            return "Error: Parametro no compatible"

        lines = ["", "="*50, "Lista de comandos", "="*50]
        for cmd in COMMANDS:
            if cmd in ("descargar", "subir"):
                lines.append(f"-{cmd} archivo")
            else:
                lines.append(f"-{cmd}")
        return "\n".join(lines)

    @staticmethod
    def _subir(parameter):
        if parameter == "None":
            return "Error: No hay archivo seleccionado"
        # TODO: implementar subida de archivo
        return "prueba"

    @staticmethod
    def _descargar(parameter):
        if parameter == "None":
            return "Error: No hay archivo seleccionado"
        
        if parameter not in ARCHIVE_LIST():
            return "Error: Archivo no encotrador"
        
        data_block_list = Archives.load_archive(parameter, side="server")
        return data_block_list
            

    @staticmethod
    def _listar(parameter):
        if parameter != "None":
            return "Error: Parametro no compatible"

        server_dir = Path("archivos_servidor")
        if not server_dir.exists():
            server_dir.mkdir(parents=True, exist_ok=True)

        lines = ["", "="*50, "Lista de archivos del servidor", "="*50]
        try:
            for i, arch in enumerate(server_dir.glob("*"), start=1):
                lines.append(f"{i}. {arch.name}")
        except OSError as e:
            return f"Error al leer directorio: {e}"

        return "\n".join(lines)

    @staticmethod
    def _listar_c(parameter):
        if parameter != "None":
            return "Error: Parametro no compatible"
        # El cliente manejara esta respuesta de forma especial
        return "info-c"
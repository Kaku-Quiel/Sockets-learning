from pathlib import Path

class Function:
    """Funciones auxiliares para el cliente."""

    @staticmethod
    def listar_c():
        """
        Retorna un listado formateado de los archivos en 'archivos_cliente'.
        Crea el directorio si no existe.
        """
        client_dir = Path("archivos_cliente")
        if not client_dir.exists():
            client_dir.mkdir(parents=True, exist_ok=True)

        lines = ["", "="*50, "Lista de archivos del cliente", "="*50]
        try:
            for i, arch in enumerate(client_dir.glob("*"), start=1):
                lines.append(f"{i}. {arch.name}")
        except OSError as e:
            return f"Error al leer directorio: {e}"

        return "\n".join(lines)
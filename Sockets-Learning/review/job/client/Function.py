from pathlib import Path


class Function:
    @staticmethod
    def info():
        string_archive_list = "\n" + "="*50 + "\nLista de archivos del cliente\n" + "="*50 + "\n"
        i = 1

        archive_list = Path("archivos_cliente").glob("*")
        for archive in archive_list:
            string_archive_list += f"{i}. {archive.name}\n"
            i += 1

        return string_archive_list
# Crea un archivo si no existe
texto = ["Linea1\n", "Linea2\n", "Linea3\n"]

try:
    with open("docs/ejercicio.txt", "x", encoding="utf-8") as archivo:
        archivo.writelines(texto)
except:
    print(f"Archivo ya creado\n")

with open("docs/ejercicio.txt", "r+", encoding="utf-8") as archivo:
    cont = archivo.read()

    print(f"Antes:\n{cont}")
    print(f"Cursor despues de leer: {archivo.tell()}")

    archivo.seek(0)
    print(f"Cursor movido al inicio: {archivo.tell()}\n")

    archivo.write(f"Inicio: {cont}")
    archivo.seek(0)
    cont = archivo.read()
    print(f"Despues:\n{cont}")

with open("docs/ejercicio.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(texto)


# Borrar el archivo
# from pathlib import Path

# archivo = Path("docs/ejercicio.txt")
# archivo.unlink()
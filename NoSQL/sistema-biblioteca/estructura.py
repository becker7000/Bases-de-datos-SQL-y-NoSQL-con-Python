import os

estructura = [
    "config",
    "modelos",
    "servicios",
    "interfaz"
]

for ruta in estructura:
    os.makedirs(ruta, exist_ok=True)

# Archivos base
archivos = [
    "main.py",
    "config/bd.py",
    "modelos/libro.py",
    "modelos/autor.py",
    "servicios/servicio_libros.py",
    "interfaz/ventana_principal.py"
]

for archivo in archivos:
    with open(archivo, "w") as f:
        f.write("# Archivo: " + archivo)

import os

estructura = [
    "config",
    "models",
    "services",
    "ui",
    "assets",
    "data/exportaciones"
]

archivos = {
    "main.py": "",
    "requirements.txt": "",
    "config/db.py": "",
    "models/__init__.py": "",
    "models/cliente.py": "",
    "models/cita.py": "",
    "services/__init__.py": "",
    "services/cliente_service.py": "",
    "services/cita_service.py": "",
    "services/exportador.py": "",
    "ui/__init__.py": "",
    "ui/main_window.py": "",
    "ui/charts.py": ""
}

for carpeta in estructura:
    os.makedirs(carpeta, exist_ok=True)

for archivo, contenido in archivos.items():
    with open(archivo, "w") as f:
        f.write(contenido)

print("✅ Proyecto generado con éxito.")

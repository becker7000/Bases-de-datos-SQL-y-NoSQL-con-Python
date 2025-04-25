import pandas as pd
from services.cita_service import obtener_citas_de_cliente
import os

def exportar_citas_a_excel(nombre_cliente, ruta="data/exportaciones/"):
    citas = obtener_citas_de_cliente(nombre_cliente)
    if not citas:
        return False

    datos = [cita.to_dict() for cita in citas]
    df = pd.DataFrame(datos)

    os.makedirs(ruta, exist_ok=True)
    nombre_archivo = f"{ruta}{nombre_cliente.replace(' ', '_')}_citas.xlsx"

    df.to_excel(nombre_archivo, index=False)
    return nombre_archivo

# services/cita_service.py

from config.db import get_clientes_collection
from models.cita import Cita

coleccion = get_clientes_collection()

def agregar_cita_a_cliente(nombre_cliente: str, cita: Cita):
    cita_dict = cita.to_dict()
    coleccion.update_one(
        {"nombre": nombre_cliente},
        {"$push": {"citas": cita_dict}}
    )

def obtener_citas_de_cliente(nombre_cliente: str):
    doc = coleccion.find_one({"nombre": nombre_cliente})
    if not doc:
        return []
    return [Cita(**c) for c in doc.get("citas", [])]

def actualizar_cita(nombre_cliente: str, index: int, nuevos_datos: dict):
    path = f"citas.{index}"
    update = {f"{path}.{k}": v for k, v in nuevos_datos.items()}
    coleccion.update_one({"nombre": nombre_cliente}, {"$set": update})

def eliminar_cita(nombre_cliente: str, index: int):
    cliente = coleccion.find_one({"nombre": nombre_cliente})
    if cliente and "citas" in cliente:
        citas = cliente["citas"]
        if index < len(citas):
            citas.pop(index)
            coleccion.update_one(
                {"nombre": nombre_cliente},
                {"$set": {"citas": citas}}
            )

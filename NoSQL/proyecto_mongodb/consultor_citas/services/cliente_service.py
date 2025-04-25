# services/cliente_service.py

from config.db import get_clientes_collection
from models.cliente import Cliente
from models.cita import Cita
from datetime import datetime

coleccion = get_clientes_collection()

def crear_cliente(cliente: Cliente):
    # Convertir el cliente a un diccionario y asegurarse de que las citas estén en formato adecuado
    cliente_dict = cliente.to_dict()

    # Convertir las fechas de las citas a string ISO si son datetime
    for cita in cliente_dict.get("citas", []):
        if isinstance(cita["fecha"], datetime):
            cita["fecha"] = cita["fecha"].isoformat()

    coleccion.insert_one(cliente_dict)

def obtener_clientes():
    clientes_raw = coleccion.find()
    clientes = []

    for doc in clientes_raw:
        c = Cliente(
            nombre=doc["nombre"],
            correo=doc["correo"],
            telefono=doc["telefono"],
            empresa=doc["empresa"]
        )
        # Aquí vamos a convertir las fechas a datetime si están en formato string
        for cita_dict in doc.get("citas", []):
            # Si la fecha está en formato ISO (string), convertirla a datetime
            if isinstance(cita_dict["fecha"], str):
                cita_dict["fecha"] = datetime.fromisoformat(cita_dict["fecha"])
            c.agregar_cita(Cita(**cita_dict))
        clientes.append(c)
    
    return clientes

def obtener_cliente_por_nombre(nombre: str):
    doc = coleccion.find_one({"nombre": nombre})
    if doc:
        cliente = Cliente(
            nombre=doc["nombre"],
            correo=doc["correo"],
            telefono=doc["telefono"],
            empresa=doc["empresa"]
        )
        # Convertir las fechas a datetime si es necesario
        for cita_dict in doc.get("citas", []):
            if isinstance(cita_dict["fecha"], str):
                cita_dict["fecha"] = datetime.fromisoformat(cita_dict["fecha"])
            cliente.agregar_cita(Cita(**cita_dict))
        return cliente
    return None

def eliminar_cliente(nombre: str):
    coleccion.delete_one({"nombre": nombre})

def actualizar_cliente(nombre: str, nuevos_datos: dict):
    coleccion.update_one({"nombre": nombre}, {"$set": nuevos_datos})

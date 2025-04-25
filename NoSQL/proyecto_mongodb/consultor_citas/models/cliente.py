from typing import List
from models.cita import Cita

class Cliente:
    def __init__(self, nombre: str, correo: str, telefono: str, empresa: str):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.empresa = empresa
        self.citas: List[Cita] = []

    def agregar_cita(self, cita: Cita):
        self.citas.append(cita)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "telefono": self.telefono,
            "empresa": self.empresa,
            "citas": [cita.to_dict() for cita in self.citas]
        }

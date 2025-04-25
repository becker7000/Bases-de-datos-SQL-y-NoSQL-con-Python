# Archivo: modelos/autor.py

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }

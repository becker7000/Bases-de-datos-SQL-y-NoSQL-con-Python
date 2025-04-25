# Archivo: modelos/libro.py

class Libro:
    def __init__(self, titulo, autor, leido=False, fecha_lectura=None):
        self.titulo = titulo
        self.autor = autor  # Diccionario con nombre y nacionalidad
        self.leido = leido
        self.fecha_lectura = fecha_lectura

    def a_diccionario(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "leido": self.leido,
            "fecha_lectura": self.fecha_lectura
        }

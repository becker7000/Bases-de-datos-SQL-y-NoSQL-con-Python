from config.bd import obtener_coleccion_libros
from modelos.libro import Libro

coleccion = obtener_coleccion_libros()

def guardar_libro(libro: Libro):
    coleccion.insert_one(libro.a_diccionario())

def obtener_libros():
    libros = []
    for doc in coleccion.find():
        libros.append(doc)
    return libros
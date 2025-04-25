import pandas as pd
from pymongo import MongoClient

# Conectar a MongoDB (por defecto en localhost y puerto 27017)
client = MongoClient('mongodb+srv://erickadmin:admin12345@mongodbcluster0.6qhwo.mongodb.net/?retryWrites=true&w=majority&appName=MongoDBCluster0')

# Crear o acceder a la base de datos (se crea automáticamente si no existe)
db = client['my_store']

# Acceder a una colección
coleccion = db['products']

# Obtener todos los productos:
productos_cursor = coleccion.find()

# Convertir los documentos a una lista de diccionarios:
productos_lista = list(productos_cursor)

# Convertir la lista de documentos a un dataframe de pandas:
dataframe_productos = pd.DataFrame(productos_lista)

# Mostrar el dataframe:
print(dataframe_productos)

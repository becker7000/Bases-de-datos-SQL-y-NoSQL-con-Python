# db.py
# python -m pip install pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI de conexión a MongoDB Atlas (debes reemplazar <db_password> con tu contraseña real)
uri = "mongodb+srv://erickadmin:12345@miprimercluster.kdfhud4.mongodb.net/?retryWrites=true&w=majority&appName=MiPrimerCluster"

# Crear cliente y conectar con el servidor de MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Función para obtener la colección de clientes
def obtener_coleccion_libros():
    try:
        # Verificar la conexión con el servidor
        client.admin.command('ping') # Silbido
        print("Se hizo ping a tu implementación. ¡Te conectaste correctamente a MongoDB!")
        
        # Conectar a la base de datos y obtener la colección de clientes
        db = client["biblioteca"]  # Asegúrate de que la base de datos sea la correcta
        return db["libros"]  # Devuelve la colección de clientes
        
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        return None

# Probar con esta línea
# obtener_coleccion_libros()
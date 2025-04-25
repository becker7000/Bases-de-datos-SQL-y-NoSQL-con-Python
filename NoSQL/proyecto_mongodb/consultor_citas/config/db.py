# db.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI de conexión a MongoDB Atlas (debes reemplazar <db_password> con tu contraseña real)
uri = "mongodb+srv://erickadmin:12345@miprimercluster.kdfhud4.mongodb.net/?retryWrites=true&w=majority&appName=MiPrimerCluster"

# Crear cliente y conectar con el servidor de MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Función para obtener la colección de clientes
def get_clientes_collection():
    try:
        # Verificar la conexión con el servidor
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        # Conectar a la base de datos y obtener la colección de clientes
        db = client["gestor_citas"]  # Asegúrate de que la base de datos sea la correcta
        return db["clientes"]  # Devuelve la colección de clientes
        
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        return None

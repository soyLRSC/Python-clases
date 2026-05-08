
import CRUD

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


MONGO_URI = "mongodb+srv://2124200328_db_user:xxxxxx@cluster0.hr2uuz8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "biblioteca"
COLLECTION_NAME= "usuarios"


def conectar_mongodb():
   
    try:
      
        client = MongoClient(MONGO_URI)
        

        client.admin.command('ping')
        print(" Conexión exitosa a MongoDB Atlas.")
        

        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        
        return collection
    except Exception as e:
        print(f"Error de conexión a MongoDB Atlas. Verifica la URI, el usuario, la contraseña y la IP en la lista blanca de Atlas: {e}")
        return None



def menu_principal():

    
    collection = conectar_mongodb()
    if collection is None:
        print("No se puede iniciar el menú sin una conexión activa a MongoDB Atlas.")
        return

    while True:
        print("\n" + "="*40)
        print("    MENÚ CRUD DE USUARIOS (MongoDB Atlas)")
        print("="*40)
        print("1.  Crear Nuevo Usuario (CREATE)")
        print("2.  Leer/Buscar Usuarios (READ)")
        print("3.   Actualizar Usuario (UPDATE)")
        print("4.   Eliminar Usuario (DELETE)")
        print("5.  Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            CRUD.menu_crear(collection)
        elif opcion == '2':
            CRUD.menu_leer(collection)
        elif opcion == '3':
            CRUD.menu_actualizar(collection)
        elif opcion == '4':
            CRUD.menu_eliminar(collection)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    # Asegúrate de instalar pymongo: pip install pymongo
    menu_principal()

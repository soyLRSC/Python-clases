#IMPORTANCION DE BCRYP PARA CIFRAR EL TOKEN
import bcrypt


#FUNCION PARA MOSTRAR DE MANERA AMIGABLE ERROR SI NO SE COLOCA ENTERO
def pedir_entero(campo):
    while True:
        valor = input(f"{campo}").strip()
        try:
            return int(valor)
        except ValueError:
            print(f" El campo '{campo}' debe ser un número entero. Intenta de nuevo.")

# Validación de flotante con mensaje amigable
def pedir_flotante(campo):
    while True:
        valor = input(f"{campo}").strip()
        try:
            return float(valor)
        except ValueError:
            print(f" El campo '{campo}' debe ser un número decimal. Intenta de nuevo.")

#validacion de texto
import re

def pedir_texto(campo):
    while True:
        texto = input(f"{campo}").strip()
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", texto):
            return texto
        else:
            print(f" El campo '{campo}' debe contener solo texto alfabético. Intenta de nuevo.")


# Validación de texto único en la colección
def pedir_texto_unico(campo, collection):
    while True:
        valor = input(f"{campo}").strip()
        if collection.find_one({campo: valor}):
            print(f" El {campo} '{valor}' ya está en uso. Elige otro.")
        else:
            return valor

# Encriptar token con bcrypt
def encriptar_token(token):
    token_bytes = token.encode('utf-8')
    salt = bcrypt.gensalt()
    token_encriptado = bcrypt.hashpw(token_bytes, salt)
    return token_encriptado.decode('utf-8')

#------------------------------------------------------------------------------------------------

def menu_crear(collection):
    print("\n--- Crear Nuevo Usuario ---")
    try:
        datos = {}
        datos["idusuario"] = pedir_entero("ID de Usuario (entero): ")
        datos["Nombre"] = pedir_texto("Nombre: ")
        datos["Paterno"] = pedir_texto("Apellido Paterno: ")
        datos["Materno"] = pedir_texto("Apellido Materno: ")
        datos["Saldo"] = pedir_flotante("Saldo (ej: 500.00): ")
        datos["nikname"] = pedir_texto_unico("nikname:", collection)
        token = input("Token:").strip()
        datos["token"] = encriptar_token(token)
        datos["idLibro"] = pedir_entero("ID de Libro (entero): ")
        datos["idsocio"] = pedir_entero("ID de Socio (entero): ")

        crear_usuario(collection, datos)
    except ValueError:
        print(" Error: Los campos 'idusuario', 'Saldo', 'idLibro' y 'idsocio' deben ser números.")
    except Exception as e:
        print(f" Error inesperado durante la creación: {e}")

def crear_usuario(collection, datos):
    try:
       resultado = collection.insert_one(datos)
       print("Usuario creado con exito")
       return resultado.inserted_id
    except Exception as e: 
        print ("error al crear usuario: {e}")
        return None
#------------------------------------------------------------------------------------------------

def menu_leer(collection): 
    
    print("n\---Buscar Usuario---" )
    opcion = input("¿Con que desea buscar al usuario?: a) ID DE USUARIO,  b) NICKNAME,  c) SALARIO, d) MOSTRAR TODO   """"""""").lower()
    if opcion == 'a': 
        try: 
            id_u = int(input("Ingrese el ID del usuario a buscar"))
            leer_usuarios(collection, {"idusuario":id_u})
        except ValueError: 
                print ("ERROR: EL ID INGRESADO NO EXISTE"+ id_u)
    elif opcion == 'b': 
        try: 
            nikname = str(input("INGRESE EL NICKNAME: "))
            leer_usuarios(collection, {"nikname": nikname})
        except ValueError: 
                print("ERROR: EL NIKNAME ES INCORRECTO O NO EXISTE"+ nikname)
    elif opcion == 'c': 
        try: 
            minimo = float(input("INTRODUZCA EL SALDO MINIMO: "))
            maximo = float(input("INTRODUZCA EL SALDO MAXIMO: "))
            filtro = {"Saldo" : {"$gte": minimo, "$lte": maximo}}
            leer_usuarios(collection, filtro)
        except ValueError: 
            print("ERROR: EL SALDO ES INCORRECTO O NO EXISTE"+ minimo)

    elif opcion == 'd':
        leer_usuarios(collection)

    else:
        print("Opción no válida. Volviendo al menú principal.")




def leer_usuarios(collection, query=None):
    if query is None:
        query = {}
    print("\n--- Resultados de la Búsqueda ---")
    try:
     # Excluir el campo 'token' de los resultados
        usuarios = collection.find(query, {"token": 0})
        encontrados = False
        for usuario in usuarios:
            print(usuario)
            encontrados = True

        if not encontrados and query:
            print("No se encontro ningun usuario en la consulta: {query}")
        elif not encontrados and not query:
            print("No hay usuarios ne la collection")

            

        return list(collection.find(query))
    except Exception as e: 
        print(f"error al leer: {e}")
        return []
    



#------------------------------------------------------------------------------------------------



def menu_eliminar(collection):
 
    print("\n--- Eliminar Usuario ---")
    try:
        id_u = int(input("Ingrese el ID de Usuario del documento a ELIMINAR: "))
        confirmacion = input(f"¿Está seguro que desea eliminar el usuario con idusuario {id_u}? (s/n): ").lower()
        
        if confirmacion == 's':
            filtro = {"idusuario": id_u}
            eliminar_usuario(collection, filtro)
        else:
            print("Operación de eliminación cancelada.")
    except ValueError:
        print(" Error: El ID de Usuario debe ser un número entero.")


def eliminar_usuario(collection, filtro):
    
    try:
        resultado = collection.delete_many(filtro)
        print(f"Usuarios eliminados: {resultado.deleted_count} documento(s) eliminado(s).")
        return resultado.deleted_count
    except Exception as e:
        print(f" Error al eliminar usuario: {e}")
        return 0
#------------------------------------------------------------------------------------------------
def actualizar_usuario(collection, filtro, nuevos_valores):
    try:
        update_operation = {"$set": nuevos_valores}
        resultado = collection.update_many(filtro, update_operation)
        print(f"Usuarios actualizados: {resultado.modified_count} documento(s) modificado(s).")
        return resultado.modified_count

    except Exception as e:
        print(f" Error al actualizar usuario: {e}")
        return 0


def menu_actualizar(collection):

    print("\n--- Actualizar Usuario ---")
    try:
        id_u = int(input("Ingrese el ID de Usuario a actualizar: "))
        filtro = {"idusuario": id_u}
        nuevos_valores = {}
        print("\nIngrese los campos a actualizar (deje vacío para omitir):")
        nombre = input("Nuevo Nombre: ")
        if nombre:
            nuevos_valores["Nombre"] = nombre

        paterno = input("Nuevo Apellido paterno: ")
        if paterno:
            nuevos_valores["Paterno"] = paterno
        
        materno = input("Nuevo apellido materno: ")
        if materno:
            nuevos_valores["Materno"] = materno
        
        saldo_str = input("Nuevo Saldo: ")
        if saldo_str:
            nuevos_valores["Saldo"] = float(saldo_str)

        nikname = input("Nuevo Nickname: ").strip()
        if nikname:
            if not collection.find_one({"nikname": nikname}):
                nuevos_valores["nikname"] = nikname
        else:
            print(f" El nickname '{nikname}' ya está en uso. Se omitirá.")

        Token = input("Nuevo Token: ")
        if Token:
            nuevos_valores["Token"] = Token
        
        idLibro = pedir_entero("Nuevo Libro: ")
        if idLibro:
            nuevos_valores["idLibro"] = idLibro

        idsocio = pedir_entero("Nuevo Socio: ")
        if idsocio:
            nuevos_valores["idsocio"] = idsocio

        if nuevos_valores:
            actualizar_usuario(collection, filtro, nuevos_valores)

        else:
            print(" No se ingresaron campos para actualizar.")
    except ValueError:
        print(" Error: El ID de Usuario y el Saldo deben ser números válidos.")

#------------------------------------------------------------------------------------------------

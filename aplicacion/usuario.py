from db import usuarios_collection

class Usuario:
    def __init__(self, nombreusuario: str, contraseña: str):
        self.nombreusuario = nombreusuario
        self.contraseña = contraseña

    def guardar_en_db(self):
        usuarios_collection.insert_one({
            "usuario": self.nombreusuario,
            "contraseña": self.contraseña
        })

    @staticmethod
    def autenticar(nombreusuario: str, contraseña: str) -> bool:
        usuario = usuarios_collection.find_one({"usuario": nombreusuario})
        return usuario and usuario["contraseña"] == contraseña
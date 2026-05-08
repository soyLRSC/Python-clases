from db import usuarios_collection

class LoginControl:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def authenticate(self):
        usuario_en_db = usuarios_collection.find_one({"usuario": self.usuario})
        if usuario_en_db and usuario_en_db["contraseña"] == self.contraseña:
            return True
        return False
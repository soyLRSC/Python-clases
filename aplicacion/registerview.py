import flet as ft
from usuario import Usuario
from db import usuarios_collection  # Asegúrate de tener esta importación

class RegisterView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Registro"
        self.page.clean()


        imagen = ft.Image(
        src="../logo.png",  # o "assets/logo.png" si es local
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN
    )
        

        self.usuario = ft.TextField(label="Nuevo usuario", width=250)
        self.contraseña = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)

        def registrar_nuevo(e):
            # Validar campos vacíos
            if not self.usuario.value or not self.contraseña.value:
                self.page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos"))
                self.page.snack_bar.open = True
                self.page.update()
                return

            # Validar si el usuario ya existe en MongoDB
            existente = usuarios_collection.find_one({"usuario": self.usuario.value})
            if existente:
                self.page.snack_bar = ft.SnackBar(ft.Text(f"El usuario '{self.usuario.value}' ya está registrado"))
                self.page.snack_bar.open = True
                self.page.update()
                return

            # Crear nuevo usuario
            nuevo_usuario = Usuario(self.usuario.value, self.contraseña.value)
            nuevo_usuario.guardar_en_db()

            # Mensaje de éxito
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Usuario '{nuevo_usuario.nombreusuario}' registrado con éxito"))
            self.page.snack_bar.open = True

            # Limpiar campos
            self.usuario.value = ""
            self.contraseña.value = ""
            self.usuario.focus()
            self.page.update()

        registro_boton = ft.ElevatedButton(text="Crear cuenta", on_click=registrar_nuevo)
        boton_login = ft.TextButton("Volver a iniciar sesión", on_click=lambda e: page.go("/"))

        self.page.add(
            ft.Column(
                controls=[
                    imagen,
                    ft.Text("Registro", size=24, weight="bold", color="blue"),
                    self.usuario,
                    self.contraseña,
                    registro_boton,
                    boton_login
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
import flet as ft
from logincontrol import LoginControl

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Login"
        self.page.clean()

        imagen = ft.Image(
            src="../logo.png",
            width=300,
            height=300,
            fit=ft.ImageFit.COVER

        )


        self.usuario = ft.TextField(label="Usuario", width=250)
        self.password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)

        def iniciar_sesion(e):
            if not self.usuario.value or not self.password.value:
                self.page.snack_bar = ft.SnackBar(ft.Text("Ingresa usuario y contraseña"))
                self.page.snack_bar.open = True
                self.page.update()
                return

            control = LoginControl(self.usuario.value, self.password.value)
            if control.authenticate():
                page.go("/home?user=" + self.usuario.value)
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"))
                self.page.snack_bar.open = True
                self.page.update()

        boton_ingresar = ft.ElevatedButton("Ingresar a sesión", on_click=iniciar_sesion)
        boton_registro = ft.TextButton("Crear cuenta nueva", on_click=lambda e: page.go("/register"))

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Zapatería", size=22, weight="bold", color="black"),
                    self.usuario,
                    self.password,
                    boton_ingresar,
                    boton_registro
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
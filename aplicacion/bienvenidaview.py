import flet as ft

class BienvenidaView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Bienvenido a la zapateria"
        self.page.clean()

        imagen = ft.Image(
            src="logo.png",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN
        )

        self.page.add(
            ft.Column(
                controls=[
                    imagen,
                    ft.Text("Bienvenido a la zapateria", size=28, weight="bold", color="black"),
                    ft.Text("Tu tienda especial", size=18),
                    ft.ElevatedButton("Iniciar sesión", on_click=lambda e: page.go("/")),
                    ft.TextButton("Crear cuenta nueva", on_click=lambda e: page.go("/register"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            )
        )

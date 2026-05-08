import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, usuario: str):
        self.page = page
        self.page.title = "Inicio"
        self.page.clean()

        fotos = [
            {"texto": "Tenis", "imagen": "logo.png"},
            {"texto": "Huaraches", "imagen": "logo.png"},
            {"texto": "Tacon", "imagen":"logo.png"},
        ]

        catalogos=[]
        for f in fotos:
            catalogo=ft.Container(
                content=ft.Column([
                    ft.Image(src=f["imagen"], width=200, height=200, fit=ft.ImageFit.CONTAIN),
                    ft.Text(f["nombre"], size=16, weight=ft.FontWeight.BOLD)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=10, 
                    border=ft.border.all(1),
                    width=180
                    )
            catalogos.append(catalogo)

        self.page.add(
            
            ft.Column(
                controls=[
                      ft.Row(controls=catalogos,wrap=True, alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column(
                      controls=[
                    
                    ft.Text(f"Bienvenido, {usuario.upper()}", size=24, weight="bold", color="blue"),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: page.go("/"))
                ],
            
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
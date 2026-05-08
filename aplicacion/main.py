import flet as ft
from loginview import LoginView
from homeview import HomeView
from registerview import RegisterView
from bienvenidaview import BienvenidaView

def main(page: ft.Page):
    page.title = "Zapateria"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 420
    page.window_height = 720
    page.bgcolor = "white"

    def route_change(e: ft.RouteChangeEvent):
        page.clean()

        if page.route == "/welcome":
            BienvenidaView(page) 

        elif page.route == "/":
            LoginView(page)  

        elif page.route == ("/register"):
            RegisterView(page)

        elif page.route.startswith("/home"):
            usuario = ""
            if "?user=" in page.route:
                usuario = page.route.split("?user=")[1]
            HomeView(page, usuario)

        elif page.route == "/register":
            RegisterView(page)

        else:
            page.add(
                ft.Column(
                    controls=[
                        ft.Text("404 - Página no encontrada", size=40, color="red"),
                        ft.ElevatedButton("Volver al inicio", on_click=lambda _: page.go("/welcome"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

    page.on_route_change = route_change
    page.go("/welcome")

ft.app(target=main)
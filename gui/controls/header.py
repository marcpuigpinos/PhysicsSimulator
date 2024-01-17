import flet as ft

def header():
    return ft.Row(
            controls=[
                ft.Text(
                    value="Particle Simulator",
                    size=30,
                    ),
                ],
            alignment=ft.MainAxisAlignment.CENTER,
            )

import flet as ft

from controls.mainpg import MainPage

def main(page: ft.Page):
    page.title = "Particle Simulator"
    page.theme_mode = "dark"
    mainpg = MainPage()
    page.add(mainpg)


ft.app(target=main)

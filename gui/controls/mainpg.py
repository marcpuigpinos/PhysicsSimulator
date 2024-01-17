import flet as ft

from .header import header
from .content import Content

class MainPage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.content = Content()

    def build(self):
        return ft.Column(
                controls=[
                        header(),
                        self.content,
                    ],
                )


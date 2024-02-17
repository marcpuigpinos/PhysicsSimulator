import flet as ft

from .header import Header
from .content import Content

class MainPage(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        self.header = Header()
        self.content = Content()

    def build(self):
        self.column_layout = ft.Column(
            controls = [
                self.header,
                self.content
            ],
            expand = True,
        )

        self.layout = ft.Container(
            content = self.column_layout,
            expand = True
        )
        
        return self.layout

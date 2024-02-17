import flet as ft

class Header(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.header_row = ft.Column(
            controls = [
                ft.Text(
                    value = "Particle Simulator",
                    size = 30,
                ),
            ],
        )

        self.layout = ft.Container(
            content = self.header_row,
            alignment = ft.alignment.center
        )

        return self.layout
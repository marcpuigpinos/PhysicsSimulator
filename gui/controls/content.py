import flet as ft

class Content(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.time = ft.Tab(text="Time")
        self.physics = ft.Tab(text="Physics")
        self.materials = ft.Tab(text="Materials")
        self.sets = ft.Tab(text="Sets")
        self.viewport = ft.Tab(text="Viewport")
        self.output = ft.Tab(text="Output")
        self.calculate = ft.Tab(text="Calculate")

    def build(self):
        menu = ft.Tabs(
                tabs=[
                    self.time,
                    self.physics,
                    self.materials,
                    self.sets,
                    self.viewport,
                    self.output,
                    self.calculate
                    ],
                expand=1
                )
        return menu


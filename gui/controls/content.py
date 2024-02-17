import flet as ft

from .pages.time_page import Time

class Content(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        
        # Time section
        self.time = ft.Tab(
            text="Time",
            content = Time(),
        )
        self.physics = ft.Tab(text="Physics")
        self.materials = ft.Tab(text="Materials")
        self.sets = ft.Tab(text="Sets")
        self.viewport = ft.Tab(text="Viewport")
        self.output = ft.Tab(text="Output")
        self.calculate = ft.Tab(text="Calculate")

    def build(self):
        self.tabs = ft.Tabs(
            tabs=[
                self.time,
                self.physics,
                self.materials,
                self.sets,
                self.viewport,
                self.output,
                self.calculate
                ],
            expand=True
        )

        self.layout = ft.Container(
            content = ft.Column(
                controls = [self.tabs],
                expand = True
            ),
            expand = True
        )
        return self.layout


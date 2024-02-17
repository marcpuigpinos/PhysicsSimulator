import flet as ft

from ..constants import __TEXT_SIZE__

class Time(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        # Total time
        self.total_time_text = ft.Text(value = "Total time:", size = __TEXT_SIZE__)
        self.total_time_field = ft.TextField(
            hint_text="Introduce the total time in seconds",
            border = ft.InputBorder.UNDERLINE,
            filled = True,
            on_change = lambda e: self.__validate_total_time(e)
        )

        self.total_time = ft.Column(
            controls = [
                self.total_time_text,
                self.total_time_field,
            ]
        )

        self.last_valid_total_time = "0"
        self.total_time_value = 0.0
        
        # Delta time
        self.delta_time_text = ft.Text(value = "Delta time:", size = __TEXT_SIZE__)
        self.delta_time_field = ft.TextField(
            hint_text="Introduce the delta time in seconds",
            border = ft.InputBorder.UNDERLINE,
            filled = True,
            on_change = lambda e: self.__validate_delta_time(e)
        )

        self.delta_time = ft.Column(
            controls = [
                self.delta_time_text,
                self.delta_time_field,
            ]
        )

        self.last_valid_delta_time = "0"
        self.delta_time_value = 0.0

    def build(self):
        self.layout_col = ft.Column(
            controls = [
                self.total_time,
                self.delta_time
            ],
            expand = True,
            spacing = 20
        )

        self.layout = ft.Container(
            content = self.layout_col,
            expand = True,
            padding = 20
        )

        return self.layout

    def __validate_total_time(self, e):
        digits = self.total_time_field.value
        if digits == "":
            self.last_valid_total_time = "0"
            self.total_time_value = 0.0
        else:
            try:
                self.total_time_value = float(digits)
                self.last_valid_total_time = digits
            except ValueError:
                self.total_time_field.value = self.last_valid_total_time
                self.total_time_value = float(self.last_valid_total_time)
                self.update()

    def __validate_delta_time(self, e):
        digits = self.delta_time_field.value
        if digits == "":
            self.last_valid_delta_time = "0"
            self.delta_time_value = 0.0
        else:
            try:
                self.delta_time_value = float(digits)
                self.last_valid_delta_time = digits
            except ValueError:
                self.delta_time_field.value = self.last_valid_delta_time
                self.delta_time_value = float(self.last_valid_delta_time)
                self.update()
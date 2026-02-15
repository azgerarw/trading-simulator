from tkinter import *
from tkinter import ttk

class ChartFormFunctions:
    def __init__(self, layout, symbol_canvas):
        self.layout = layout
        self.symbol_canvas = symbol_canvas
        self.update_chart_callback = None

    def check(self, option):
               
        if option in self.layout.period_options:
                current_period = option
                print(current_period)
        elif option in self.layout.interval_options:
                current_interval = option
                print(current_interval)
    
    def on_update_chart(self):
        period = self.layout.period_var.get()
        interval = self.layout.interval_var.get()
        if self.update_chart_callback:
            self.update_chart_callback(
                period,
                interval
            )
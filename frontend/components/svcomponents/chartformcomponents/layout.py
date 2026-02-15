from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

class Layout:
    def __init__(self, container, symbol, symbol_canvas):
        self.period_options = ["1d", "7d", "1mo"]
        self.period_var = StringVar(value="")
        self.current_period = StringVar(value="")
        self.current_interval = StringVar(value="")
        self.interval_options = ["1m", "5m", "15m", "1h", "1d"]
        self.interval_var = StringVar(value="")
        self.functions = None

    def build_form(self, container, symbol):

        create_chart_form = Frame(container, pady=10)
        create_chart_form.grid(row=2,column=0)

        create_chart_form_gap = Label(create_chart_form, height=1)
        create_chart_form_gap.grid(row=1,column=0)

        create_chart_button_gap = Label(create_chart_form, width=10)
        create_chart_button_gap.grid(row=1, column=10)

        periods_label = Label(create_chart_form, text="select period")
        periods_label.grid(row=0, column=0)

        intervals_label = Label(create_chart_form, text="select interval")
        intervals_label.grid(row=0, column=4)

        for col, option in enumerate(self.period_options):
                rb = ttk.Radiobutton(
                create_chart_form,
                text=option,
                variable=self.period_var,
                value=option,
                bootstyle="primary-toolbutton",
                command=lambda opt=option: self.functions.check(opt)
                )
                rb.grid(row=0, column=col + 1, padx=4)
                rb.columnconfigure(col, weight=1)

        for col, option in enumerate(self.interval_options):
                rb = ttk.Radiobutton(
                create_chart_form,
                text=option,
                variable=self.interval_var,
                value=option,
                bootstyle="primary-toolbutton",
                command=lambda opt=option: self.functions.check(opt)
                )
                rb.grid(row=0, column=col + 5, padx=4)
                rb.columnconfigure(col, weight=1)

        create_chart_button = ttk.Button(create_chart_form, bootstyle="primary", text="update", command=self.functions.on_update_chart)
        create_chart_button.grid(row=0, column=10)

    def set_functions(self, functions):
        self.functions = functions
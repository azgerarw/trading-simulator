from tkinter import *
from frontend.gui.create_gui.create_account_gui import open_top_window
from backend.users.login import login
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

import pandas as pd

class Layout2:
    def __init__(self, login_frame, root):
        self.login_frame = login_frame
        self.root = root
        self.on_build_chart = None

    def build(self):

        frame_2 = Frame(self.login_frame, width=800, height=800, background="black")
        frame_2.grid(row=0, column=1, sticky="nsew")

        for i in range(1):
            frame_2.columnconfigure(i, weight=1)
        for r in range(2): 
            frame_2.rowconfigure(r, weight=1)

        frame_2_1 = Frame(frame_2, width=600, height=200, background="black")
        frame_2_1.grid(row=0, column=0, sticky="nsew")
        
        for i in range(5):
            frame_2_1.columnconfigure(i, weight=1)
        for r in range(5): 
            frame_2_1.rowconfigure(r, weight=1)
        
        title_frame_2 = Label(frame_2_1, background="black", text="Trading Simulator", font=("Monospace", 30, "bold"), fg="white", justify="center").grid(row=3, column=2)
        

        self.login_canvas = Canvas(
            frame_2,
            width=700,
            height=500,
            highlightthickness=0
        )
        self.login_canvas.grid(row=1, column=0, sticky='nsew')
        
        self.login_canvas.create_rectangle(10, 20, 680, 520)


        
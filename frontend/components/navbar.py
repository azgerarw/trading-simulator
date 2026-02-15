from tkinter import *
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import backend.users.state as state

class Navbar:
    def __init__(self):
        self.frame1 = None
        self.user_label = None
        self.empty_label = None
        self.balance_label = None
        self.on_logout = None
        self.menu = None
        self.var = StringVar(value="Menu")
        self.values = ["Menu", "Home", "Positions", "Deposit", "Withdraw", "Profile", "Logout"]
        self.on_select = None

    def build(self, frame):

        self.frame1 = Frame(frame, height=50, width=900, pady=20, padx=20)
        self.frame1.grid(row=0,column=0, sticky="nsew")
        self.username = state.current_user[2] if state.current_user else ""
        self.wallet = state.user_wallet[3] if state.user_wallet else 0
        

        for c in range(3):
            self.frame1.columnconfigure(c, weight=1)
        
        self.user_label = Label(self.frame1, text=f"Welcome {self.username}!", anchor="w")
        self.user_label.grid(row=0, column=0, sticky="nsew")


        self.balance_label = Label(self.frame1, text=f"Balance: {self.wallet:.2f}$", anchor="n")
        self.balance_label.grid(row=0, column=1, sticky="nsew")

        self.menu = ttk.OptionMenu(self.frame1, self.var, *self.values, 
                                   bootstyle="primary-outline",
                                   command=lambda v: self.on_select(v))
        
        self.menu.grid(row=0, column=2, sticky="e")
        self.menu.configure(width=7)

    def check_option(self, value, pages):

        if value == "Logout":
            pages["login"][0].tkraise()
        elif value == "Home":
            pages["home"][0].tkraise()
            pages["home"][1].frame1.layout.refresh()
        elif value == "Positions":
            pages["positions"][1].view.layout_frame1.refresh()
            pages["positions"][0].tkraise()
        elif value == "Deposit":
            pages["deposit"][1].view.layout_frame1.refresh()
            pages["deposit"][0].tkraise()
        elif value == "Withdraw":
            pages["withdraw"][1].view.layout_frame1.refresh()
            pages["withdraw"][0].tkraise()
        else:
            pages["profile"][1].view.layout_frame1.refresh()
            pages["profile"][0].tkraise()
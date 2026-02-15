from frontend.gui.change_password.change_password import open_cp_window
from frontend.gui.create_gui.create_account_gui import open_top_window
from backend.users.login import login
from tkinter import *

import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

class Layout1:
    def __init__(self, login_frame, root, pages):
        self.login_frame = login_frame
        self.root = root
        self.pages = pages


    def build(self):

        frame_1 = Frame(self.login_frame, width=300, height=600)
        frame_1.grid(row=0, column=0, sticky="nsew")
        
        for i in range(5):
            frame_1.columnconfigure(i, weight=1)
        for r in range(30): 
            frame_1.rowconfigure(r, weight=1)

        title = Label(frame_1, text="Enter account details", width=25, justify="center").grid(row=8, column=1, columnspan=3)
        create_account = Label(frame_1, text="Create account", width=25, justify="center")
        create_account.grid(row=27, column=1, columnspan=3)
        create_account.bind("<Button-1>", lambda e: open_top_window(self.root))
        
        forgot_password = Label(frame_1, text="Change password", width=25, justify="center")
        forgot_password.grid(row=28, column=1, columnspan=3)
        forgot_password.bind("<Button-1>", lambda e: open_cp_window(self.root))

        input_email = Entry(frame_1, width=25, border=1, justify="left")
        input_email.grid(row=9, column=1, columnspan=3)
        input_password = Entry(frame_1, width=25, border=1, justify="left", show="*")
        input_password.grid(row=10, column=1, columnspan=3)

        login_button = ttk.Button(frame_1, width=23, text="Log In", command= lambda: login(input_email, input_password, self.pages)).grid(row=11, column=1, columnspan=3)
        
        

    
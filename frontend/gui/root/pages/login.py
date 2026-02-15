from tkinter import *
from backend.presenters.login.login_presenter import LoginPresenter
from frontend.gui.create_gui.create_account_gui import open_top_window
from backend.users.login import login
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import random
import pandas as pd

def login_page(root, container, pages=None):

    login_page_frame = Frame(container, width=900, height=600)
    login_page_frame.grid(row=0, column=0, sticky="nsew")
    login_page_frame.columnconfigure(0, weight=1)
    login_page_frame.rowconfigure(0, weight=1)

    presenter = LoginPresenter(layout=login_page_frame, root=root, pages=pages)

    return [login_page_frame, presenter]
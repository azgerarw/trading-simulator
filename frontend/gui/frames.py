from tkinter import *
import backend.states.pages as pages_state
from frontend.gui.root.pages.deposit import deposit_page
from frontend.gui.root.pages.login import login_page
from frontend.gui.root.pages.home import home_page
from frontend.gui.root.pages.positions import positions_page
from frontend.gui.root.pages.profile import profile_page
from frontend.gui.root.pages.withdraw import withdraw_page

def init_frames(root):
    container = Frame(root, width=900, height=600)
    container.pack(fill="both", expand=True)
    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=1)
    
    pages = {}

    pages["login"] = login_page(root, container, pages)
    pages["home"]  = home_page(root, container, pages)
    pages["positions"] = positions_page(root, container, pages)
    pages["deposit"] = deposit_page(root, container, pages)
    pages["profile"] = profile_page(root, container, pages)
    pages["withdraw"] = withdraw_page(root, container, pages)

    pages_state.pages = pages
    pages["login"][0].tkraise()

    return pages
    
    
from collections.abc import Iterable
from tkinter import *
from tkinter.ttk import Combobox, Separator, Treeview
from backend.presenters.home.home_presenter import HomePresenter
import backend.users.state as state
from backend.db.db import db
from tkinter import ttk
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import yfinance as yf # type: ignore
from frontend.gui.symbol.symbol import open_symbol_window
from frontend.views.homeview.frame1 import Frame1View
from frontend.views.homeview.frame2_1 import Frame2_1View
from frontend.views.homeview.frame2_2 import Frame2_2View

def home_page(root, container, pages=None):
    
    
    
    home_page_frame = Frame(container, width=900, height=600)
    
    presenter = HomePresenter(home_container=home_page_frame, root=root, pages=pages)

    return [home_page_frame, presenter]
from tkinter import *
from backend.presenters.positions.positions_presenter import PositionsPresenter
import backend.users.state as state
from backend.db.db import db
from tkinter import ttk
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import yfinance as yf # type: ignore
from frontend.gui.symbol.symbol import open_symbol_window

def positions_page(root, container, pages):
    
    positions_page_frame = Frame(container, width=900, height=600)
    
    presenter = PositionsPresenter(container=positions_page_frame, root=root, pages=pages)

    return [positions_page_frame, presenter]
from datetime import time
from tkinter import *
import yfinance as yf # type: ignore
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import *

from backend.presenters.symbol_presenter import SymbolPresenter # type: ignore

def open_symbol_window(root, symbol):

        symbol_window = Toplevel(root, padx=20, pady=20)
        symbol_window.title(f"{symbol}")
        
        presenter = SymbolPresenter(symbol, symbol_window)

 
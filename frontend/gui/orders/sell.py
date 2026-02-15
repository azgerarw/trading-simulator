from tkinter import *
from tkinter import ttk
from backend.presenters.orders.sellpresenter import SellPresenter
import backend.users.state as state

def open_sell_order_window(root, symbol, df):
        
    sell_presenter = SellPresenter(root, symbol, df)
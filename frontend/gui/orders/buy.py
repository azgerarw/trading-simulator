from tkinter import *
from tkinter import ttk
from backend.presenters.orders.buypresenter import BuyPresenter
import backend.users.state as state

def open_buy_order_window(root, symbol, df):
        
    buy_presenter = BuyPresenter(root, symbol, df)

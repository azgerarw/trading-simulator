from tkinter import *
from backend.presenters.deposit.deposit_presenter import DepositPresenter
import backend.users.state as state
from backend.db.db import db
from tkinter import ttk
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import yfinance as yf # type: ignore

def deposit_page(root, container, pages):

    
    
    deposit_page_frame = Frame(container, width=900, height=600)
    
    presenter = DepositPresenter(container=deposit_page_frame, root=root, pages=pages)

    return [deposit_page_frame,presenter]
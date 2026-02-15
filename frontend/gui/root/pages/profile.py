from tkinter import *
from backend.presenters.profile.profile_presenter import ProfilePresenter
import backend.users.state as state
from backend.db.db import db
from tkinter import ttk
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import yfinance as yf # type: ignore

def profile_page(root, container, pages):

    

    profile_page_frame = Frame(container, width=900, height=600)

    presenter = ProfilePresenter(container=profile_page_frame, root=root, pages=pages)

    return [profile_page_frame, presenter]
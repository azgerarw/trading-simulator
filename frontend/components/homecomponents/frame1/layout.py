from backend.models.users.user import User
import backend.users.state as state
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import *

from frontend.components.navbar import Navbar # type: ignore

class Layout:
    def __init__(self):
        
        self.navbar = Navbar()
        self.wallet = state.user_wallet[3] if state.user_wallet else 0  

    def build(self, home_page_frame):

        self.navbar.build(home_page_frame)

        return self
    
    def refresh(self):
        
        self.wallet = User().fetch_wallet(state.current_user[0], 'USD')

        self.navbar.balance_label.config(text=f"Balance: {self.wallet[4]:.2f}$")
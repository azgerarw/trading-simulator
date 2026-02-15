from backend.models.users.user import User
import backend.users.state as state
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import *

from frontend.components.navbar import Navbar # type: ignore

class Layout1:
    def __init__(self, container, root, pages):
        self.container = container
        self.navbar = Navbar()
        self.wallet = state.user_wallet[3] if state.user_wallet else 0  

    def build(self):

        self.navbar.build(self.container)

        return self
    
    def refresh(self):
        
        self.wallet = User().fetch_wallet(state.current_user[0], 'USD')

        self.navbar.user_label.config(text="User profile")
        self.navbar.balance_label.config(text=f"Balance: {self.wallet[4]:.2f}$")
from tkinter import *
from tkinter import ttk
from backend.models.users.user import User
import backend.users.state as state

class Layout:
    def __init__(self, root, symbol, df):
        self.root = root
        self.symbol = symbol
        self.df = df
        self.buy_window = None
        self.buy_window_frame = None
        self.symbol_label = None
        self.last_price_label = None
        self.rb_market = None
        self.rb_limit = None
        self.quantity_label = None
        self.qty_var = None
        self.buy_button = None
        self.quantity_box = None
        self.available_label = None
        self.total_var = None
        self.rb_var = None
        self.available_var = None

    def build(self):

        self.wallet = User().fetch_wallet(state.current_user[0], 'USD')
        self.available_var = self.wallet[4]
        
        self.buy_window = Toplevel(self.root)
        self.buy_window.title(f"{self.symbol}: buy order")
        
        self.buy_window_frame = Frame(self.buy_window, padx=20, pady=20, width=300, height=400)
        self.buy_window_frame.grid(row=0, column=0, sticky="nsew")
        self.buy_window_frame.grid_propagate(False)
        for row in range(7):
            self.buy_window_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.buy_window_frame.columnconfigure(col, weight=1)

        self.symbol_label = Label(self.buy_window_frame, anchor="center", text=f"{self.symbol} / USD")
        self.symbol_label.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.last_price_label = Label(self.buy_window_frame, anchor="center", text=f"Last price: {self.df.iloc[-1]["Close"]:.2f}$")
        self.last_price_label.grid(row=1, column=0, sticky="nsew", columnspan=2)

        self.rb_var = StringVar(value="")
        self.rb_market = ttk.Radiobutton(
            self.buy_window_frame,
            text="Market",
            value="MARKET",
            variable=self.rb_var,
            bootstyle="primary"
        )
        self.rb_market.grid(row=2, column=0, pady=4, sticky="n")

        self.rb_limit = ttk.Radiobutton(
            self.buy_window_frame,
            text="Limit",
            bootstyle="primary",
            state="disabled"
        )
        self.rb_limit.grid(row=2, column=1, pady=4, sticky="n")

        self.quantity_label = Label(self.buy_window_frame, text="Quantity", anchor="center")
        self.quantity_label.grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.total_var = StringVar(value="Total: 0")

        self.total_label = Label(self.buy_window_frame, textvariable=self.total_var)
        self.total_label.grid(row=5, column=0, columnspan=2, sticky="nsew")

        self.qty_var = StringVar(value="0")

        self.quantity_box = ttk.Spinbox(
            self.buy_window_frame,
            from_=0,
            to=100,
            width=5,
            textvariable=self.qty_var,
            bootstyle="primary"
        )
        self.quantity_box.grid(row=4, column=0, columnspan=2)

        self.available_label = Label(self.buy_window_frame, text=f"Available: {self.wallet[4]:.2f}$",anchor="center")
        self.available_label.grid(row=6, column=0, columnspan=2, sticky="nsew")

        self.buy_button = ttk.Button(self.buy_window_frame, bootstyle="primary", text="Buy")
        self.buy_button.grid(row=7, column=0, columnspan=2, sticky="nsew")

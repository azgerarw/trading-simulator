from backend.models.positions.positions import Positions
from backend.models.svmodels.symbol_component import SymbolData
import backend.users.state as state
from tkinter import ttk
from tkinter import *
from frontend.gui.symbol.symbol import open_symbol_window
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
import backend.states.pages as pages_state

class Layout2:
    def __init__(self, container, root, pages, sibling_frame1):
        self.sibling = sibling_frame1
        self.container = container
        self.root = root
        self.pages = pages
        self.frame_1 = None
        self.on_logout = None
        self.menu = None
        self.var = StringVar(value="Menu")
        self.values = ["Menu", "Home", "Positions", "Deposit", "Withdraw", "Profile", "Logout"]
        self.even = 0
        self.odd = 1
        self.positions = []
        
    def build(self):
        self.frame2 = Frame(self.container, width=900, pady=20, padx=20)
        self.frame2.grid(row=1,column=0, sticky="n")
        
        for col in range(4):
            self.frame2.columnconfigure(col, weight=1)

        self.render_positions()
        
    def render_positions(self):

        for widget in self.frame2.winfo_children():
            widget.destroy()
            
        if not self.positions:

            no_data_label = ttk.Labelframe(self.frame2, text='No data found', padding=20)
            no_data_label.grid(row=0, column=0, sticky='n')

            message_label = Label(no_data_label, text='No positions were found in this account', anchor='center')
            message_label.grid(row=0, column=0)
        else:
            self.positions_scrollbar = Scrollbar(self.frame2, orient="vertical")
            self.positions_scrollbar.grid(row=0, column=4, sticky="ns")

            self.positions_canvas = Canvas(self.frame2, height=550, width=700, bg="#fafafa",
                                yscrollcommand=self.positions_scrollbar.set)
            self.positions_canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")

            self.positions_scrollbar.config(command=self.positions_canvas.yview)


            self.positions_container = Frame(self.positions_canvas, bg="#fafafa", pady=20, padx=20)
            self.positions_container.grid(row=0, column=0, sticky='n')

            id = self.positions_canvas.create_window(
                (0, 0),
                window=self.positions_container,
                anchor="n"
            )

            self.positions_canvas.update_idletasks()

            self.positions_canvas_width = self.positions_canvas.winfo_width()
            self.frame2_width = self.positions_container.winfo_reqwidth()

            x = (self.positions_canvas_width - self.frame2_width) // 2
            self.positions_canvas.coords(id, x, 0)

        
        for i, p in enumerate(self.positions):

            self.odd = self.odd + 2
            self.even = self.even + 2
            info = SymbolData(p[0]).ticker().info
            current_price = info.get("currentPrice") or info.get("regularMarketPrice") or ''

            pl = (current_price - p[2]) * p[1]
            pl = int(pl)

            color = "#26a69a" if pl > 0 else "white" if pl == 0 else "#ef5350"

            button = ttk.Button(self.positions_container, bootstyle="primary", text=p[0], command=lambda sy=p[0]: open_symbol_window(self.root, sy))

            position = ttk.Labelframe(self.positions_container, width=600, height=50, padding=10, bootstyle="primary", labelwidget=button, labelanchor="n")
            position.grid(row=self.odd, column=0, sticky="ew")
            
            for col in range(8):
                position.columnconfigure(col, weight=1)

            separator = Label(self.positions_container, height=2)
            separator.grid(row=self.even, column=0)

            ticker_label = Label(position, text=p[0], anchor="center", padx=5, pady=5)
            ticker_label.grid(row=0, column=0)

            quantity_label = Label(position, text=p[1], anchor="center", padx=5, pady=8)
            quantity_label.grid(row=0, column=1)

            average_price_label = Label(position, text=f'{p[2]:.2f}', anchor="center", padx=5, pady=5)
            average_price_label.grid(row=0, column=2)

            current_price_label = Label(position, text=f'{current_price:.2f}', anchor="center", padx=5, pady=5)
            current_price_label.grid(row=0, column=3)

            PL_label = Label(position, text=pl, anchor="center", padx=5, pady=5)
            PL_label.grid(row=0, column=4)
            PL_label.config(fg=color)

            buy_button = ttk.Button(position, text='BUY', bootstyle='success', command=lambda sy=p[0]: self.on_buy(sy))
            buy_button.grid(row=0, column=5)

            gap_label = Label(position, anchor="center", padx=5, pady=5)
            gap_label.grid(row=0, column=6)

            sell_button = ttk.Button(position, text='SELL', bootstyle='danger', command=lambda sy=p[0]: self.on_sell(sy))
            sell_button.grid(row=0, column=7)

            self.positions_container.update_idletasks()
            self.positions_canvas.config(scrollregion=self.positions_canvas.bbox("all"))


    def refresh(self):
        if not state.current_user:
            return

        self.positions = Positions(state.current_user[0]).fetch()
        self.render_positions()
        self.sibling.refresh()
        pages_state.pages["home"][1].frame1.layout.refresh()
        pages_state.pages["profile"][1].view.layout_frame2.refresh()
        pages_state.pages["deposit"][1].view.layout_frame1.refresh()
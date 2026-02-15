from tkinter import Toplevel
from backend.models.positions.positions import Positions
from backend.models.svmodels.symbol_component import SymbolData
from frontend.gui.orders.buy import open_buy_order_window
from frontend.gui.orders.sell import open_sell_order_window
from frontend.views.positions.view import View
import backend.users.state as state

class PositionsPresenter:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.view = View(container=self.container, root=self.root, pages=self.pages)

        self.view.layout_frame1.navbar.on_select = self.on_selected_option
        self.view.layout_frame2.on_sell = self.sell
        self.view.layout_frame2.on_buy = self.buy

        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.container.rowconfigure(1, weight=20)

    def on_selected_option(self, value):

        self.view.layout_frame1.navbar.check_option(value, self.pages)

    def sell(self, symbol):

        df = SymbolData(symbol=symbol).fetch()

        open_sell_order_window(self.root, symbol, df)

    def buy(self, symbol):

        df = SymbolData(symbol=symbol).fetch()

        open_buy_order_window(self.root, symbol, df)

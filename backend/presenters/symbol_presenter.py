import time
from backend.models.svmodels.symbol_component import SymbolData
from frontend.views.symbolview.change_chart import ChangeChartView
from frontend.views.symbolview.mini_symbol_chart import MiniChartView
from frontend.views.symbolview.news import NewsView
from frontend.views.symbolview.symbol_chart_view import SymbolChartView
from tkinter import *
from tkinter import ttk
from frontend.gui.orders.buy import open_buy_order_window

class SymbolPresenter:
    def __init__(self, symbol, root):
        self.root = root
        self.symbol = symbol
        self.df = None
        self.chart = None
        self.mini_chart = None
        self.container = Frame(root)
        self.scrollbar = Scrollbar(self.container, orient="horizontal")
        self.canvas = Canvas(self.container, width=800, height=400, bg="#fafafa", xscrollcommand=self.scrollbar.set)
        self.price_canvas = Canvas(
            self.container,
            width=50,
            height=400,
            bg="#fafafa",
            highlightthickness=0
        )
        self.symbol_canvas = Canvas(
                self.container,
                width=300,
                height=400,
                bg="#fafafa",
                highlightthickness=0
        )
        self.mini_chart_canvas = Canvas(self.symbol_canvas, width=220, height=190, bg="lightgray")
        self.chart_form = ChangeChartView(container=self.container, symbol=symbol, symbol_canvas=self.symbol_canvas)
        
        self.chart_form.functions.update_chart_callback = self.on_update_chart

        self.container.grid(row=0, column=0)

        self.scrollbar.grid(row=1, column=0, sticky="ew")

        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.price_canvas.grid(row=0, column=1, sticky="ns")

        self.symbol_canvas.grid(row=0, column=2, sticky="ns")

        self.df = SymbolData(symbol)
        self.df = self.df.fetch()
        
        self.chart = SymbolChartView(canvas=self.canvas, price_canvas=self.price_canvas, df=self.df)

        self.mini_chart = MiniChartView(mini_chart_canvas=self.mini_chart_canvas, symbol_canvas=self.symbol_canvas, df=self.df.tail(14), symbol=self.symbol)

        self.news = NewsView(container=self.container, symbol=self.symbol)

        self.scrollbar.config(command=self.canvas.xview)
        
        self.on_update_chart = self.on_update_chart

        self.start_update_loop()

        self.buy_window = None
        self.mini_chart.layout.on_open_buy_window = self.open_buy_window

        
    def on_update_chart(self, period, interval):

        self.df = SymbolData(self.symbol)
        self.df = self.df.fetch(period=period, interval=interval)

        self.canvas.delete("all")
        self.price_canvas.delete("all")
        self.mini_chart_canvas.delete("all")
        self.symbol_canvas.delete("all")

        self.chart = SymbolChartView(
            canvas=self.canvas,
            price_canvas=self.price_canvas,
            df=self.df
        )

        self.mini_chart = MiniChartView(
            mini_chart_canvas=self.mini_chart_canvas,
            symbol_canvas=self.symbol_canvas,
            df=self.df.tail(14),
            symbol=self.symbol
        )

        self.mini_chart.layout.on_open_buy_window = self.open_buy_window
        
        self.symbol_canvas.create_window(
            40, 110,
            window=self.mini_chart_canvas,
            anchor="nw"
        )

        self.canvas.update_idletasks()
        self.canvas.config(
            scrollregion=(0, 0, self.chart.candles.total_width, self.chart.grid.chart_height + self.chart.scaler.padding * 2)
        )

    def start_update_loop(self):
        self._update()

    def _update(self):
        self.on_update_chart("1d", "1m")
        self.container.after(15000, self._update)

    def open_buy_window(self):
        open_buy_order_window(self.root, self.symbol, self.df)
        

    
           
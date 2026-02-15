from collections.abc import Iterable
import time
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
from backend.models.svmodels.symbol_component import SymbolData
from frontend.gui.orders.buy import open_buy_order_window
from frontend.gui.symbol.symbol import open_symbol_window

class CreateFrames:
    def __init__(self, all, frame2_2, container, root, list_frame):
        self.root = root
        self.data = all
        self.frame2_2 = frame2_2
        self.container = container
        self.list_frame = list_frame
        self.loading = None
        self.scrollbar = None
        self.canvas = None
        self.new_list_frame = None
        self.list_frame_id = None
        self.canvas_width = None
        self.frame_width = None
        self.center_list_frame = self.center_list_frame
        self.loading = Label(frame2_2, text="Loading...", pady=10, fg="white")
        self.loading.grid(row=2, column=1)
        

        self.frame2_2.update_idletasks()
        
        self.scrollbar = Scrollbar(self.container, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.canvas = Canvas(self.container, yscrollcommand=self.scrollbar.set, width=800, height=500)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.scrollbar.config(command=self.canvas.yview)

        self.list_frame.destroy()
        row1 = 1
        row2 = 0
        self.new_list_frame = Frame(self.canvas, pady=20, padx=20)
        self.list_frame_id = self.canvas.create_window((0, 0), window=self.new_list_frame, anchor="n")

        self.canvas.bind("<Configure>", self.center_list_frame)

        self.new_list_frame.bind("<Configure>", self.on_configure)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        if isinstance(self.data, Iterable) and not hasattr(self.data, "iterrows"):
            for symbol in self.data:
                history = SymbolData(symbol=symbol).fetch()

                if history.empty:
                    print(f"No data found")
                    continue

                

                frame = ttk.Labelframe(self.new_list_frame, height=350, width=300, bootstyle="primary", padding=5)
                frame.grid_propagate(False)
                frame.grid_columnconfigure(0, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                mini_chart_card_canvas = Canvas(frame, width=250, height=200)
                mini_chart_card_canvas.grid(row=3, column=0, columnspan=2, sticky="n")

                mini_chart_card_canvas.create_rectangle(
                        1, 1,
                        249, 189,
                        outline="#e0e0e0",
                        width=1,
                        tags=("mini_chart",)
                )

                MINI_HEIGHT = 170
                MINI_PADDING = 10

                def mini_price_to_y(price):
                        return MINI_PADDING + (mini_max - price) / (mini_max - mini_min) * MINI_HEIGHT

                last_15 = history.tail(15)
                candle_width = 10
                mini_max = last_15["High"].max()
                mini_min = last_15["Low"].min()

                for i, row in enumerate(last_15.itertuples()):

                        x = 15 + i * (candle_width + 4)

                        open_y  = mini_price_to_y(row.Open)
                        close_y = mini_price_to_y(row.Close)
                        high_y  = mini_price_to_y(row.High)
                        low_y   = mini_price_to_y(row.Low)

                        color = "#49ff39" if row.Close >= row.Open else "#fa0800"

                        mini_chart_card_canvas.create_line(
                        x + candle_width//2, high_y,
                        x + candle_width//2, low_y,
                        fill=color,
                        tags=("mini_chart",)
                        )

                        mini_chart_card_canvas.create_rectangle(
                        x, min(open_y, close_y),
                        x + candle_width, max(open_y, close_y),
                        fill=color,
                        outline=color,
                        tags=("mini_chart",)
                        )
                
                button = ttk.Button(frame, text=symbol, bootstyle="primary", command=lambda sy=symbol: open_symbol_window(self.root, sy))
                frame.config(labelwidget=button, labelanchor="n")
                frame.grid(row=row1,column=0)
                
                buy_button = ttk.Button(frame, text="Buy", bootstyle="primary", command= lambda sy=symbol, root=self.root, df=history:open_buy_order_window(root, sy, df))
                buy_button.grid(row=4, column=0, sticky="n")
                sell_button = ttk.Button(frame, text="Sell", bootstyle="primary", state="disabled")
                sell_button.grid(row=4, column=1, sticky="n")

                separator = Label(self.new_list_frame, height=2)
                separator.grid(row=row2, column=0)
                row1 += 2
                row2 = row1 - 1
                inner_row = 0


                ticker = SymbolData(symbol).ticker()

                last_price = history["Close"].iloc[-1]
                
                open_price = history["Open"].iloc[0]

                price_change = ((last_price - open_price) / open_price) * 100

                color = "#26a69a" if price_change > 0 else "#ef5350"

                short_name = ticker.info["shortName"]
                short_name_label = Label(frame, text=f"${short_name}", fg="blue", justify="center", pady=4)
                short_name_label.grid(row=1, column=0, columnspan=3)

                price_label = Label(frame, text=f"${last_price:.2f}", fg="blue", justify="center", pady=4)
                price_label.grid(row=2, column=0, sticky="n")

                price_change_label = Label(frame, text=f"{price_change:.2f}%", justify="center", pady=4)
                price_change_label.grid(row=2, column=1, sticky="n")
                price_change_label.config(fg=color)

                self.loading.grid_remove()
                self.frame2_2.update_idletasks()
        
        else:    
        
            for idx, data_row in self.data.iterrows():

                history = SymbolData(symbol=idx).fetch()

                if history.empty:
                    print(f"No data found")
                    continue
                
                
                frame = ttk.Labelframe(self.new_list_frame, height=350, width=300, bootstyle="primary", padding=5)
                frame.grid_propagate(False)
                frame.grid_columnconfigure(0, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                mini_chart_card_canvas = Canvas(frame, width=250, height=200)
                mini_chart_card_canvas.grid(row=3, column=0, columnspan=2, sticky="n")

                mini_chart_card_canvas.create_rectangle(
                        1, 1,
                        249, 189,
                        outline="#e0e0e0",
                        width=1,
                        tags=("mini_chart",)
                )

                MINI_HEIGHT = 170
                MINI_PADDING = 10

                def mini_price_to_y(price):
                        return MINI_PADDING + (mini_max - price) / (mini_max - mini_min) * MINI_HEIGHT

                last_15 = history.tail(15)
                candle_width = 10
                mini_max = last_15["High"].max()
                mini_min = last_15["Low"].min()

                for i, row in enumerate(last_15.itertuples()):

                        x = 15 + i * (candle_width + 4)

                        open_y  = mini_price_to_y(row.Open)
                        close_y = mini_price_to_y(row.Close)
                        high_y  = mini_price_to_y(row.High)
                        low_y   = mini_price_to_y(row.Low)

                        color = "#49ff39" if row.Close >= row.Open else "#fa0800"

                        mini_chart_card_canvas.create_line(
                        x + candle_width//2, high_y,
                        x + candle_width//2, low_y,
                        fill=color,
                        tags=("mini_chart",)
                        )

                        mini_chart_card_canvas.create_rectangle(
                        x, min(open_y, close_y),
                        x + candle_width, max(open_y, close_y),
                        fill=color,
                        outline=color,
                        tags=("mini_chart",)
                        )
                
                button = ttk.Button(frame, text=idx, bootstyle="primary", command=lambda sy=idx: open_symbol_window(self.root, sy))
                frame.config(labelwidget=button, labelanchor="n")
                frame.grid(row=row1,column=0)
                
                buy_button = ttk.Button(frame, text="Buy", bootstyle="primary")
                buy_button.grid(row=4, column=0, sticky="n")
                sell_button = ttk.Button(frame, text="Sell", bootstyle="primary", state="disabled")
                sell_button.grid(row=4, column=1, sticky="n")

                separator = Label(self.new_list_frame, height=2)
                separator.grid(row=row2, column=0)
                row1 += 2
                row2 = row1 - 1


                ticker = SymbolData(idx).ticker()

                last_price = history["Close"].iloc[-1]
                
                open_price = history["Open"].iloc[0]

                price_change = ((last_price - open_price) / open_price) * 100

                color = "#26a69a" if price_change > 0 else "#ef5350"

                short_name = ticker.info["shortName"]
                short_name_label = Label(frame, text=f"${short_name}", fg="blue", justify="center", pady=4)
                short_name_label.grid(row=1, column=0, columnspan=3)

                price_label = Label(frame, text=f"${last_price:.2f}", fg="blue", justify="center", pady=4)
                price_label.grid(row=2, column=0, sticky="n")

                price_change_label = Label(frame, text=f"{price_change:.2f}%", justify="center", pady=4)
                price_change_label.grid(row=2, column=1, sticky="n")
                price_change_label.config(fg=color)
        
                self.loading.grid_remove()
                self.frame2_2.update_idletasks()          

    def center_list_frame(self, event=None):
            self.canvas.update_idletasks()

            self.canvas_width = self.canvas.winfo_width()
            self.frame_width = self.new_list_frame.winfo_reqwidth()

            x = (self.canvas_width - self.frame_width) // 2
            self.canvas.coords(self.list_frame_id, x, 0)

    def on_configure(self, event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))    
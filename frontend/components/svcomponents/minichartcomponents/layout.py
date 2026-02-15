from tkinter import messagebox


class LayoutMiniChart:
    def __init__(self, symbol_canvas, mini_chart_canvas):
        self.symbol_canvas = symbol_canvas
        self.mini_chart_canvas = mini_chart_canvas
        self.candles_box = None
        self.symbol_text = None
        self.borders = None
        self.last_price_text = None
        self.buy_rect = None
        self.buy_text = None
        self.sell_rect = None
        self.sell_text = None
        self.on_open_buy_window = None

    def draw(self, df, symbol):
        self.candles_box = self.mini_chart_canvas.create_rectangle(
            1, 1,
            219, 189,
            outline="#e0e0e0",
            width=1,
            tags=("mini_chart",)
        )

        self.symbol_text = self.symbol_canvas.create_text(
            150, 20,
            anchor="n",
            text=f"{symbol}",
            font=("Segoe UI", 20, "bold"),
            fill="#5df5f5"
        )

        self.borders = self.symbol_canvas.create_rectangle(
            10, 10,
            290, 390, outline="#e0e0e0"
        )

        self.last_price_text = self.symbol_canvas.create_text(
            150, 60,
            anchor="n",
            text=f"{df["Close"].iloc[-1]:.2f}",
            font=("Segoe UI", 20, "bold"),
            fill="blue"
        )

        self.buy_rect = self.symbol_canvas.create_rectangle(
            60, 320,
            140, 350,
            outline="blue",
            width=2,
            tags=("buy",),
            fill="blue"
        )

        self.buy_text = self.symbol_canvas.create_text(
            100, 335,
            text="BUY",
            fill="white",
            font=("Segoe UI", 10, "bold"),
            tags=("buy",)
        )

        self.sell_rect = self.symbol_canvas.create_rectangle(
            160,
            320,
            240,
            350,
            outline="gray",
            width=2,
            tags=("sell",),
            fill="gray"
        )

        self.sell_text = self.symbol_canvas.create_text(
            200, 335,
            text="SELL",
            fill="white",
            font=("Segoe UI", 10, "bold"),
            tags=("sell",)
        )

        self.symbol_canvas.create_window(
            40, 110,
            window=self.mini_chart_canvas,
            anchor="nw"
        )

    def on_click(self, event):

        tags = self.symbol_canvas.gettags("current")

        if "buy" in tags and self.on_open_buy_window:
            self.on_open_buy_window()
        elif "sell" in tags:
            messagebox.showinfo('feature not available', 'Sell positions are currently not available')
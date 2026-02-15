class PriceLabels:
    def __init__(self, canvas, price_canvas, scaler, df):
        self.canvas = canvas
        self.price_canvas = price_canvas
        self.scaler = scaler
        self.price_label = None
        self.current_price_box = None
        self.current_price_label = None
        self.last_price = None
        self.h_line = None
        self.total_width = None

    def draw(self, df):
        self.last_price = df["Close"].iloc[-1]
        self.total_width = self.scaler.padding + len(df) * (10 + 2)

        self.price_label = self.price_canvas.create_text(
            40, 0,
            anchor="e",
            text="",
            font=("Segoe UI", 9, "bold"),
            fill="white"
        )

        self.current_price_label = self.price_canvas.create_text(
                40,
                self.scaler.price_to_y(self.last_price),
                anchor="e",
                text=f"{self.last_price:.2f}",
                font=("Segoe UI", 9),
                fill="blue"
        )

        self.current_price_box = self.price_canvas.create_rectangle(
            0,
            self.scaler.price_to_y(self.last_price) - 10,
            41,
            self.scaler.price_to_y(self.last_price) + 10,
            outline="blue"
        )

        self.h_line = self.canvas.create_line(
        0,
        self.scaler.price_to_y(self.last_price),
        self.total_width,
        self.scaler.price_to_y(self.last_price),
        fill="blue",
        dash=(4, 2)
    )
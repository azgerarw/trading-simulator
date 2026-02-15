class GridLayer:
    def __init__(self, canvas, scaler, df, price_canvas):
        self.price_steps = 10
        self.price_range = scaler.max_price - scaler.min_price
        self.step = self.price_range / self.price_steps
        self.canvas = canvas
        self.scaler = scaler
        self.chart_height = 360
        self.price_canvas = price_canvas

    def draw(self, df):
        for i in range(self.price_steps + 1):
            price = self.scaler.min_price + i * self.step
            y = self.scaler.price_to_y(price)

            self.canvas.create_line(
                self.scaler.padding,
                y,
                5000,
                y,
                fill="#e0e0e0"
            )
        
        for i in range(self.price_steps + 1):
            price = self.scaler.min_price + i * self.step
            y = self.scaler.price_to_y(price)

            self.canvas.create_line(
                self.scaler.padding,
                y,
                5000,
                y,
                fill="#e0e0e0"
            )

            self.price_canvas.create_text(
                40,
                y,
                anchor="e",
                text=f"{price:.2f}",
                font=("Segoe UI", 9),
                fill="white"
            )
class Candles:
    def __init__(self, df, scaler, mini_chart_canvas):
        self.scaler = scaler
        self.mini_chart_canvas = mini_chart_canvas
        self.candle_width = 10
        
    def draw(self, df):
        for i, row in enumerate(df.itertuples()):

            x = 15 + i * (self.candle_width + 4)

            open_y  = self.scaler.mini_price_to_y(row.Open)
            close_y = self.scaler.mini_price_to_y(row.Close)
            high_y  = self.scaler.mini_price_to_y(row.High)
            low_y   = self.scaler.mini_price_to_y(row.Low)

            color = "green" if row.Close >= row.Open else "red"

            self.mini_chart_canvas.create_line(
                x + self.candle_width//2, high_y,
                x + self.candle_width//2, low_y,
                fill=color,
                tags=("mini_chart",)
            )

            self.mini_chart_canvas.create_rectangle(
                x, min(open_y, close_y),
                x + self.candle_width, max(open_y, close_y),
                fill=color,
                outline=color,
                tags=("mini_chart",)
            )

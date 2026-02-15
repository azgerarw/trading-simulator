class CandleLayer:
    def __init__(self, canvas, scaler, df):
        self.candles = []
        self.canvas = canvas
        self.scaler = scaler
        self.candle_width = 10
        self.total_width =  self.scaler.padding + len(df) * (10 + 2)

    
    
    def build(self, df):
        for i, row in enumerate(df.itertuples()):

            x = self.scaler.padding + i * (self.candle_width + 2)

            open_y  = self.scaler.price_to_y(row.Open)
            close_y = self.scaler.price_to_y(row.Close)
            high_y  = self.scaler.price_to_y(row.High)
            low_y   = self.scaler.price_to_y(row.Low)

            wick = self.canvas.create_line(
                x + self.candle_width//2, high_y,
                x + self.candle_width//2, low_y
            )

            top = min(open_y, close_y)
            bottom = max(open_y, close_y)

            color = "green" if row.Close >= row.Open else "red"

            body = self.canvas.create_rectangle(
                x, top,
                x + self.candle_width, bottom,
                fill=color,
                outline=color
            )

            self.candles.append({
                "x": x,
                "open": row.Open,
                "close": row.Close,
                "high": row.High,
                "low": row.Low,
                "body": body,
                "wick": wick
            })

    def update(self, df):
        for i, row in enumerate(df.tail(len(self.candles)).itertuples()):
            candle = self.candles[i]
            x = self.scaler.padding + i * (self.candle_width + 2)
            open_y  = self.scaler.price_to_y(row.Open)
            close_y = self.scaler.price_to_y(row.Close)
            high_y  = self.scaler.price_to_y(row.High)
            low_y   = self.scaler.price_to_y(row.Low)

            self.canvas.coords(
                candle["wick"],
                x + self.candle_width//2, high_y,
                x + self.candle_width//2, low_y
            )

            self.canvas.coords(
                candle["body"],
                x, min(open_y, close_y),
                x + self.candle_width, max(open_y, close_y)
            )

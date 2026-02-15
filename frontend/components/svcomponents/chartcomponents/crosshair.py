class Crosshair:
    def __init__(self, canvas, price_canvas, scaler, ohlc, candle_layer):
       self.canvas = canvas
       self.price_canvas = price_canvas
       self.scaler = scaler
       self.ohlc = ohlc
       self.candle_layer = candle_layer
       self.active_candle = None
       self.price_label = None
       self.horizontal_price_line = None
       self.vertical_price_line = None

    def draw_lines(self):

        self.horizontal_price_line = self.canvas.create_line(0, 0, 0, 0, fill="#888888", dash=(2, 2))
        self.vertical_price_line = self.canvas.create_line(0, 0, 0, 0, fill="#888888", dash=(2, 2))

    def move(self, event):
        x = self.canvas.canvasx(event.x)
        y = event.y

        price = self.scaler.y_to_price(y)

        self.canvas.coords(
            self.horizontal_price_line,
            0, y,
            self.candle_layer.total_width, y
        )

        self.canvas.coords(
            self.vertical_price_line,
            x, 0,
            x, self.candle_layer.total_width
        )
        
        self.price_canvas.coords(self.price_label, 40, y)
        self.price_canvas.itemconfig(self.price_label, text=f"{price:.2f}")

        index = int((x - self.scaler.padding) // (self.candle_layer.candle_width + 2))

        if 0 <= index < len(self.candle_layer.candles):
            candle = self.candle_layer.candles[index]

            if self.active_candle != candle:

                if self.active_candle:
                    self.canvas.itemconfig(self.active_candle["body"], width=1)

                self.canvas.itemconfig(candle["body"], width=2)
                self.active_candle = candle

                self.ohlc.move(event)
                self.ohlc.update(candle)
    

class OHLCOverlay:
    def __init__(self, canvas):
        self.canvas = canvas
        self.offset_x = 50
        self.offset_y = 30
        self.box_width = 70
        self.box_height = 80
        self.box = None
        self.text = None

    def create_box(self):

        self.box = self.canvas.create_rectangle(
                    5, 5,
                    155, 85
        )

        self.text = self.canvas.create_text(
            10, 10,
            anchor="nw",
            text="",
            font=("Segoe UI", 9)
        )

 
    def move(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        x1 = x - self.offset_x
        y1 = y + self.offset_y
        x2 = x1 + self.box_width
        y2 = y1 + self.box_height

        self.canvas.coords(self.box, x1, y1, x2, y2)
        self.canvas.coords(self.text, x1 + 9, y1 + 7)

    def update(self, candle):
        text = (
            f"O: {candle['open']:.2f}\n"
            f"H: {candle['high']:.2f}\n"
            f"L: {candle['low']:.2f}\n"
            f"C: {candle['close']:.2f}"
        )

        color = "#26a69a" if candle["close"] >= candle["open"] else "#ef5350"
        self.canvas.itemconfig(self.box, outline=color)
        self.canvas.itemconfig(self.text, fill=color, text=text)
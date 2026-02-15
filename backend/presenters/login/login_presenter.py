from frontend.views.login.view import View
import random

class LoginPresenter:
    def __init__(self, layout, root, pages):
        self.layout = layout
        self.root = root
        self.pages = pages
        self.view = View(container=self.layout, root=self.root, pages=self.pages)
        self.view.layout_frame2.on_build_chart = self.build_chart
        self.TOP = 40
        self.BOTTOM = 450
        self.HEIGHT = self.BOTTOM - self.TOP
        self.view.layout_frame2.on_build_chart()

    def price_to_y(self, price, prices):
            
            max_price = max(prices)
            min_price = min(prices)

            return self.BOTTOM - (price - min_price) / (max_price - min_price) * self.HEIGHT
    
    def build_chart(self):
        
        start_price=100
        volatility=0.15
        data = []
        price = start_price

        for i in range(25):

            x = 20 + i * (20 + 2)

            open_price = price

            change = open_price * random.uniform(-volatility, volatility)
            close_price = open_price + change

            high = max(open_price, close_price) * (1 + random.uniform(0, 0.500))
            low  = min(open_price, close_price) * (1 - random.uniform(0, 0.200))

            data.append({
                "Open": open_price,
                "High": high,
                "Low": low,
                "Close": close_price
            })

            price = close_price

        
            

            prices = [d["High"] for d in data] + [d["Low"] for d in data]
            

            
            
            for i, candle in enumerate(data):

                x = 20 + i * (20 + 6)

                open_y  = self.price_to_y(candle["Open"], prices)
                close_y = self.price_to_y(candle["Close"], prices)
                high_y  = self.price_to_y(candle["High"], prices)
                low_y   = self.price_to_y(candle["Low"], prices)

                color = "green" if candle["Close"] >= candle["Open"] else "red"

                self.view.layout_frame2.login_canvas.create_line(
                    x + 10, high_y,
                    x + 10, low_y,
                    fill=color
                )

                self.view.layout_frame2.login_canvas.create_rectangle(
                    x,
                    min(open_y, close_y),
                    x + 20,
                    max(open_y, close_y),
                    fill=color,
                    outline=color
                )

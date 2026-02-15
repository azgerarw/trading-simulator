class PriceScaler:
    def __init__(self, df):
        self.min_price = df["Low"].min()
        self.max_price = df["High"].max()
        self.chart_height = 360
        self.padding = 20

    def price_to_y(self, price):
        return self.padding + (self.max_price - price) / (self.max_price - self.min_price) * self.chart_height

    def y_to_price(self, y):
        return self.max_price - ((y - self.padding) / self.chart_height) * (self.max_price - self.min_price)

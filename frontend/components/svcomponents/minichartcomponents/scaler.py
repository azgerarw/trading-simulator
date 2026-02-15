class PriceScaler:
    def __init__(self, df):
        self.mini_height = 170
        self.mini_padding = 10
        self.mini_min = df["Low"].min()
        self.mini_max = df["High"].max()

    def mini_price_to_y(self, price):
        return self.mini_padding + (self.mini_max - price) / (self.mini_max - self.mini_min) * self.mini_height

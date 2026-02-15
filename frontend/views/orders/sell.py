from frontend.components.orders.sell_layout import Layout

class SellView:
    def __init__(self, root, symbol, df):
        self.layout = Layout(root, symbol, df)

        self.layout.build()

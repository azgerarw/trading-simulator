from frontend.components.orders.buy_layout import Layout

class BuyView:
    def __init__(self, root, symbol, df):
        self.layout = Layout(root, symbol, df)

        self.layout.build()

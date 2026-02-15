import yfinance as yf  # type: ignore
class News:
    def __init__(self, symbol):
        self.symbol = symbol

    def fetch(self):
        return yf.Ticker(self.symbol).get_news(10)
 

import yfinance as yf # type: ignore

class Lookup:
    def __init__(self, value):
        self.df = yf.Lookup(value).get_all(count=5)
import yfinance as yf # type: ignore

class Sector:
    def __init__(self, value):
        self.sector = yf.Sector(value)
        self.industry = yf.Industry(value.lower())
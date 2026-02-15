import yfinance as yf  # type: ignore

class SymbolData:
    def __init__(self, symbol):
        self.symbol = symbol
        
    def fetch(self, interval="1m", period="1d"):
        return yf.Ticker(self.symbol).history(interval=interval, period=period)
    
    def ticker(self):
        return yf.Ticker(self.symbol)
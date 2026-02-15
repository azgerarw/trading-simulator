class Options:
    def __init__(self):
        self.options = ["Forex", "Cryptocurrencies", "Etfs", "Index", "Stocks"]
        self.markets = {
            "forex": [ 
            "EURUSD=X",
            "USDJPY=X",
            "GBPUSD=X",
            "AUDUSD=X",
            "USDCAD=X",
            "USDCHF=X",
            "NZDUSD=X"
        ],
        "indexes": [
            "^GSPC",
            "^DJI",
            "^IXIC",
            "^RUT",
            "^FTSE",
            "^GDAXI",
            "^FCHI",
            "^N225",
            "^HSI"
        ],
        "cryptocurrencies": [
            "BTC-USD",
            "ETH-USD",
            "USDT-USD",
            "BNB-USD",
            "SOL-USD",
            "XRP-USD",
            "USDC-USD",
            "ADA-USD",
            "DOGE-USD",
            "AVAX-USD"
        ],
        "etfs": [
            "SPY",
            "QQQ",
            "VTI",
            "VOO",
            "DIA",
            "IWM",
            "EFA",
            "EM",
            "GLD",
            "TLT"
        ],
        "stocks":  [
            "AAPL", 
            "TSLA", 
            "NVDA", 
            "AMD", 
            "META", 
            "AMZN", 
            "MSFT"
        ]
        }
        self.companies_options = ["top_companies", "top_growth_companies", "top_performing_companies"]
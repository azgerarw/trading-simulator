from frontend.components.svcomponents.minichartcomponents.scaler import PriceScaler
from frontend.components.svcomponents.minichartcomponents.candles import Candles
from frontend.components.svcomponents.minichartcomponents.layout import LayoutMiniChart

class MiniChartView:
    def __init__(self, mini_chart_canvas, symbol_canvas, df, symbol):
        self.scaler = PriceScaler(df=df)
        self.layout = LayoutMiniChart(mini_chart_canvas=mini_chart_canvas, symbol_canvas=symbol_canvas)
        self.candles = Candles(df=df, scaler=self.scaler, mini_chart_canvas=mini_chart_canvas)
    
        self.layout.draw(df, symbol)
        self.candles.draw(df)
        

        symbol_canvas.tag_bind("buy", "<Button-1>", self.layout.on_click)
        symbol_canvas.tag_bind("sell", "<Button-1>", self.layout.on_click)


    
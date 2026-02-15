from frontend.components.svcomponents.chartcomponents.candle_layer import CandleLayer
from frontend.components.svcomponents.chartcomponents.price_scaler import PriceScaler
from frontend.components.svcomponents.chartcomponents.grid_layer import GridLayer
from frontend.components.svcomponents.chartcomponents.OHLCOverlay import OHLCOverlay
from frontend.components.svcomponents.chartcomponents.crosshair import Crosshair
from frontend.components.svcomponents.chartcomponents.price_labels import PriceLabels

class SymbolChartView:
    def __init__(self, canvas, price_canvas, df):
        self.scaler = PriceScaler(df=df)
        self.candles = CandleLayer(canvas=canvas, scaler=self.scaler, df=df)
        self.grid = GridLayer(canvas=canvas, scaler=self.scaler, df=df, price_canvas=price_canvas)
        self.ohlc = OHLCOverlay(canvas=canvas)
        self.crosshair = Crosshair(canvas=canvas, price_canvas=price_canvas, scaler=self.scaler, ohlc=self.ohlc, candle_layer=self.candles)
        self.price_labels = PriceLabels(price_canvas=price_canvas, scaler=self.scaler, df=df, canvas=canvas)

        self.grid.draw(df)
        self.candles.build(df)
        self.ohlc.create_box()
        self.crosshair.draw_lines()
        self.price_labels.draw(df)
        self.crosshair.price_label = self.price_labels.price_label

        canvas.config(
            scrollregion=(0, 0, self.candles.total_width, self.grid.chart_height + self.scaler.padding * 2)
        )
        canvas.xview_moveto(1.0)

        canvas.bind("<Motion>", self.crosshair.move)

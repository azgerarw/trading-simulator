from frontend.components.svcomponents.chartformcomponents.functions import ChartFormFunctions
from frontend.components.svcomponents.chartformcomponents.layout import Layout

class ChangeChartView:
    def __init__(self, container, symbol, symbol_canvas):
        self.layout = Layout(container=container, symbol=symbol, symbol_canvas=symbol_canvas)
        self.functions = ChartFormFunctions(
            layout=self.layout,
            symbol_canvas=symbol_canvas
        )

        self.layout.set_functions(self.functions)
        self.layout.build_form(container, symbol)

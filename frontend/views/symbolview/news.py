from frontend.components.svcomponents.newscomponents.layout import Layout

class NewsView:
    def __init__(self, container, symbol):
        self.container = container
        self.layout = Layout(container=container, symbol=symbol)

        self.layout.create_news()
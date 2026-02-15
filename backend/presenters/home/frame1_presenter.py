class Frame1Presenter:
    def __init__(self, layout, pages):
        self.pages = pages
        self.layout = layout
        self.layout.navbar.on_select = self.on_selected_option

   

    def on_selected_option(self, value):

        self.layout.navbar.check_option(value, self.pages)
            
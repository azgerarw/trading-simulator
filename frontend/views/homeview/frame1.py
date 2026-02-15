from frontend.components.homecomponents.frame1.layout import Layout


class Frame1View:
    def __init__(self, home_page_container):
        self.homecontainer = home_page_container
        self.layout = Layout()

        self.layout.build(home_page_frame=self.homecontainer)
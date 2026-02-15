from tkinter import Frame
from frontend.components.profile.layout_frame1 import Layout1
from frontend.components.profile.layout_frame2 import Layout2
import backend.users.state as state

class View:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        
        self.layout_frame1 = Layout1(container=self.container, root=self.root, pages=self.pages)
        self.layout_frame2 = Layout2(container=self.container, root=self.root, pages=self.pages)

        self.layout_frame1.build()
        self.layout_frame2.build()
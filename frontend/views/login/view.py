from tkinter import Frame
from frontend.components.login.layout_frame1 import Layout1
from frontend.components.login.layout_frame2 import Layout2

class View:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages        
        
        self.layout_frame1 = Layout1(login_frame=self.container, root=self.root, pages=self.pages)
        self.layout_frame2 = Layout2(login_frame=self.container, root=self.root)
        
        self.layout_frame1.build()
        self.layout_frame2.build()


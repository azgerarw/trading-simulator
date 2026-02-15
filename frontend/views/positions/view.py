from tkinter import Frame
from frontend.components.positions.layout_frame1 import Layout1
from frontend.components.positions.layout_frame2 import Layout2
from backend.models.positions.positions import Positions
import backend.users.state as state

class View:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        
        
        self.layout_frame1 = Layout1(container=self.container, root=self.root, pages=self.pages)
        self.layout_frame2 = Layout2(container=self.container, root=self.root, pages=self.pages, sibling_frame1=self.layout_frame1)
        
        self.layout_frame1.build()
        self.layout_frame2.build()
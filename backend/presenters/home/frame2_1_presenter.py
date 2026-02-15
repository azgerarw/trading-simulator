from tkinter import ttk
from tkinter import *

from backend.models.homemodels.lookup import Lookup
from backend.models.homemodels.markets import Options
from frontend.components.homecomponents.frame2.frame2_2.createframes import CreateFrames

class Frame2_1Presenter:
    def __init__(self, layout, root, frame2_2, container, list_frame):
        self.root = root
        self.frame2_2 = frame2_2
        self.container = container
        self.list_frame = list_frame
        self.layout = layout
        self.layout.on_cancel_search = self.cancel_search
        self.layout.on_filter_selected = self.check
        self.layout.on_search = self.search


    def cancel_search(self):

        self.layout.cancel_search_button.grid_remove()
        
        self.layout.search_bar.delete(0, END)

        self.layout.rb_frame.grid()


    def search(self, value):
        all = Lookup(value).df
        
        frames = CreateFrames(all=all, frame2_2=self.frame2_2, root=self.root, container=self.container, list_frame=self.list_frame)

        self.layout.rb_frame.grid_remove()

        self.layout.cancel_search_button.grid()
        

    def check(self, option):
        if option == "Forex":
            data = Options().markets["forex"]
            
        elif option == "Cryptocurrencies":
            data = Options().markets["cryptocurrencies"]
            
        elif option == "Etfs":
            data = Options().markets["etfs"]
            
        elif option == "Index":
            data = Options().markets["indexes"]
            
        else:
            data = Options().markets["stocks"]
            
        frames = CreateFrames(all=data, frame2_2=self.frame2_2, root=self.root, container=self.container, list_frame=self.list_frame)


from tkinter import ttk
from tkinter import *

from backend.models.homemodels.sector import Sector
from frontend.components.homecomponents.frame2.frame2_1.layout import Layout
from frontend.components.homecomponents.frame2.frame2_2.createframes import CreateFrames

class Frame2_2Presenter:
    def __init__(self, layout, frame2_1, root, frame2_2, container, list_frame):
        self.root = root
        self.layout = layout
        self.frame2_2 = frame2_2
        self.container = container
        self.list_frame = list_frame
        self.rb_frame_2 = None
        self.filter_var = StringVar(value="")
        self.layout.on_industry_selected = self.show_industry
        self.frame2_1 = frame2_1
        self.start_update_loop()

    def check(self, ind, opt):

            ind = Sector(ind).industry
            if opt == "top_companies":
                data = ind.top_companies.index
            elif opt == "top_performing_companies":
                data = ind.top_performing_companies.index
            else:
                data = ind.top_growth_companies.index

            frames = CreateFrames(data, frame2_2=self.frame2_2, root=self.root, container=self.container, list_frame=self.list_frame)

    def show_industry(self, industry):
        self.layout.list_frame.destroy()
        self.frame2_1.layout.rb_frame.grid_remove()
        
        rb_frame_2 = Frame(self.frame2_1.layout.frame2_1)
        rb_frame_2.grid(row=2,column=0)

        options3 = ["top_companies", "top_growth_companies", "top_performing_companies"]

        def back():
            rb_frame_2.grid_remove()
            self.frame2_1.layout.rb_frame.grid()

        back_button = ttk.Button(rb_frame_2, bootstyle="secondary", text="back", command=back)
        back_button.grid(row=2, column=5)

        for col, option in enumerate(options3):
            rb = ttk.Radiobutton(
                rb_frame_2,
                text=option,
                variable=self.filter_var,
                value=option,
                bootstyle="primary-toolbutton",
                command=lambda opt=option, ind=industry: self.check(ind, opt)
            )
            rb.grid(row=2, column=col, padx=4)
            rb.columnconfigure(col, weight=1)

    
    def start_update_loop(self):
        self._update_frame()
    
    def _update_frame(self):
        self.list_frame.update_idletasks()
        self.list_frame.after(3000, self._update_frame)
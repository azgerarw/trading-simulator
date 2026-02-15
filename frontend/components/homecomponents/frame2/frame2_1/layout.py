from tkinter import ttk
from tkinter import *

from backend.models.homemodels.markets import Options

class Layout:
    def __init__(self, frame2):
        self.frame2 = frame2
        self.frame2_1 = Frame(frame2, height=50, width=900)
        self.rb_frame = Frame(self.frame2_1)
        self.filter_var = StringVar(value="")
        self.separator_searchbar = Label(self.frame2_1, height=1)
        self.options = Options().options
        self.selected_option = StringVar(value=self.options[0])
        self.searchbar_frame = Frame(self.frame2_1, width=450)
        self.search_bar = ttk.Entry(self.searchbar_frame, width=30, bootstyle="primary")
        self.on_search = None
        self.search_bar_button = ttk.Button(self.searchbar_frame, text="search", bootstyle="primary", command=lambda: self.on_search and self.on_search(self.search_bar.get()))
        

        self.rb_frame.grid(row=2,column=0)
        self.frame2_1.grid(row=0, column=0)
        self.separator_searchbar.grid(row=1, column=0)
    
        self.searchbar_frame.grid(row=0, column=0)
        self.searchbar_frame.columnconfigure(1, pad=5)
        self.searchbar_frame.columnconfigure(0, pad=5)

        self.search_bar.grid(row=0, column=0)
        self.search_bar_button.grid(row=0, column=1)

        self.on_filter_selected = None
        self.on_cancel_search = None

        self.cancel_search_button = ttk.Button(self.frame2_1, text="Cancel Search", bootstyle="secondary", command=lambda: self.on_cancel_search and self.on_cancel_search())
        self.cancel_search_button.grid(row=3, column=0)
        self.cancel_search_button.grid_remove()

        for r in range(2):
            self.frame2_1.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame2_1.columnconfigure(c, weight=1)

        for col, option in enumerate(self.options):
            rb = ttk.Radiobutton(
                self.rb_frame,
                text=option,
                variable=self.filter_var,
                value=option,
                bootstyle="primary-toolbutton",
                command=lambda opt=option: (
                    self.on_filter_selected and self.on_filter_selected(opt)
                )
            )
            rb.grid(row=2, column=col, padx=4)
            rb.columnconfigure(col, weight=1)

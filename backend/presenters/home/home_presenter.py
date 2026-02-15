from backend.presenters.home.frame1_presenter import Frame1Presenter
from backend.presenters.home.frame2_1_presenter import Frame2_1Presenter
from backend.presenters.home.frame2_2_presenter import Frame2_2Presenter
from frontend.views.homeview.frame1 import Frame1View
from tkinter import ttk
from tkinter import *

from frontend.views.homeview.frame2_1 import Frame2_1View
from frontend.views.homeview.frame2_2 import Frame2_2View

class HomePresenter:
    def __init__(self, home_container, root, pages):
        self.pages = pages
        self.root = root
        self.home_container = home_container
        self.frame1 = Frame1View(home_page_container=home_container)
        self.frame2 = Frame(home_container, height=550, width=900)
        self.frame2_1 = Frame2_1View(frame2=self.frame2)
        self.frame2_2 = Frame2_2View(frame2=self.frame2, frame2_1=self.frame2_1)
        self.frame1_presenter = Frame1Presenter(pages=self.pages, layout=self.frame1.layout)
        self.frame2_1_presenter = Frame2_1Presenter(layout=self.frame2_1.layout, root=self.root, frame2_2=self.frame2_2.layout.frame2_2, container=self.frame2_2.layout.container, list_frame=self.frame2_2.layout.list_frame)
        self.frame2_2_presenter = Frame2_2Presenter(layout=self.frame2_2.layout, frame2_1=self.frame2_1, root=self.root, frame2_2=self.frame2_2.layout.frame2_2, container=self.frame2_2.layout.container, list_frame=self.frame2_2.layout.list_frame)

        self.home_container.grid(row=0, column=0, sticky="nsew")
        self.home_container.rowconfigure(0, weight=1)

        self.home_container.rowconfigure(1, weight=75)
        self.home_container.columnconfigure(0, weight=1)

        self.frame2.grid(row=1, column=0, sticky="nsew")

        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=50)

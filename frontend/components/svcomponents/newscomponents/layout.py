from tkinter import *
from tkinter import ttk

from backend.models.svmodels.news import News

class Layout:
    def __init__(self, container, symbol):
        self.container = container
        self.symbol = symbol
        self.news_container = None
        self.news_scrolbar = None
        self.news_canvas = None

    def create_news(self):    
        self.news_scrollbar = Scrollbar(self.container, orient="vertical")
        self.news_scrollbar.grid(row=3, column=4, sticky="ns")

        self.news_canvas = Canvas(self.container, height=180, bg="#fafafa",
                            yscrollcommand=self.news_scrollbar.set)
        self.news_canvas.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.news_scrollbar.config(command=self.news_canvas.yview)


        self.news_container = Frame(self.news_canvas, bg="#fafafa")

        self.news_canvas.create_window(
            (0, 0),
            window=self.news_container,
            anchor="nw"
        )

        news = News(self.symbol).fetch()

        for i in range(len(news)):

            col = 0 if i < 5 else 2
            row = i if i < 5 else i - 5

            new_container = Frame(self.news_container, width=550, height=200)
            new_container.grid(row=row, column=col, padx=10, pady=5)
            new_container.grid_propagate(False)

            item = news[i]["content"]

            Label(
                new_container,
                text=item["title"],
                wraplength=560,
                font=("Segoe UI", 10, "bold"),
                justify="left"
            ).grid(row=0, column=0, sticky="w")

            Label(
                new_container,
                text=item["summary"],
                wraplength=560,
                pady=5,
                padx=5,
                justify="left"
            ).grid(row=1, column=0, sticky="w")

            Label(
                new_container,
                text=item["pubDate"],
                font=("Segoe UI", 7),
                fg="gray"
            ).grid(row=3, column=0, sticky="w")

            Label(
                new_container,
                text=item["canonicalUrl"]["url"],
                font=("Segoe UI", 8, "bold"),
                fg="blue",
                justify="left"
            ).grid(row=2, column=0, sticky="w")
            
        self.news_container.update_idletasks()
        self.news_canvas.config(scrollregion=self.news_canvas.bbox("all"))
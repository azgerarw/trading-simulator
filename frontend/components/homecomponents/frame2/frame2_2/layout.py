from tkinter import ttk
from tkinter import *

from ttkbootstrap import Treeview

from backend.models.homemodels.sector import Sector

class Layout:
    def __init__(self, frame2, frame2_1):
        self.frame2_2 = Frame(frame2, width=900)
        self.sectors = {
            "basic-materials": [], 
            "communication-services": [],
            "consumer-cyclical": [],
            "consumer-defensive": [],
            "energy": [],
            "financial-services": [],
            "healthcare": [],
            "industrials": [],
            "real-estate": [],
            "technology": [],
            "utilities": []
        }
        self.sector_nodes = {}
        self.sectors_tree = Treeview(
            self.frame2_2,
            selectmode="browse",
            columns=("sector",),
            bootstyle="primary",
            show="tree headings",
            height=11,
            padding=5
        )
        self.container = Frame(self.frame2_2, width=800, height=500)
        self.frame2 = frame2
        self.list_frame = Frame(self.frame2_2)
        
        for item in self.sectors.items():
            sector = Sector(item[0])
            data = sector.sector.industries
            for idx, data_row in data.iterrows():
                self.sectors[item[0]].append(idx)

        self.frame2_2.grid(row=2, column=0)
        self.container.grid(row=2, column=1, sticky="nsew")
        self.sectors_tree.grid(row=2, column=0, sticky="new")
        self.sectors_tree.heading("#0", text="Sectors")

        self.sectors_tree.column("#0", minwidth=50, anchor="w", stretch=True)
        self.sectors_tree.column("#1", width=1, anchor="w")

        self.on_industry_selected = None

        for item in self.sectors.items():
            iid = self.sectors_tree.insert(
                "", "end",
                text=item[0],
                values=("",)
            )
            self.sector_nodes[item[0]] = iid
        
        for item in self.sectors.items():
            
            for industry in item[1]:
                self.sectors_tree.insert(
                    self.sector_nodes[item[0]],
                    "end",
                    text=industry,
                    values=("",)
                )

        def on_tree_click(event):
            item_id = self.sectors_tree.focus()
            if not item_id:
                return

            industry = self.sectors_tree.item(item_id, "text")
            parent = self.sectors_tree.parent(item_id)

            if parent and self.on_industry_selected:
                self.on_industry_selected(industry)


        self.sectors_tree.bind("<<TreeviewSelect>>", on_tree_click)
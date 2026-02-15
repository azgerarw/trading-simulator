from datetime import datetime
from tkinter import messagebox
from backend.models.orders.sell import SellOrder
from backend.models.positions.positions import Positions
from frontend.gui.root import pages
from frontend.views.orders.sell import SellView
from backend.db.db import db
import backend.users.state as state
import backend.states.pages as pages_state

class SellPresenter:
    def __init__(self, root, symbol, df):
        self.view = SellView(root, symbol, df)
        self.on_qty_change = self.on_qty_change
        self.view.layout.qty_var.trace_add("write", self.on_qty_change)
        self.on_sb_press = self.on_sb_press
        self.view.layout.sell_button.config(command=self.on_sb_press)
        self.quantity = None
        self.price = None
        self.total = None
        self.execute_sell = self.execute_sell

    def on_qty_change(self, *args):
            try:
                self.quantity = int(self.view.layout.qty_var.get())
                self.price = float(self.view.layout.df.iloc[-1]["Close"])
                self.total = self.quantity * self.price
                self.view.layout.total_var.set(f"Total: {self.total:.2f}$")
            except ValueError:
                self.view.layout.total_var.set("Total: -")

    def on_sb_press(self):
        if self.view.layout.rb_var.get() != "MARKET":
            messagebox.showinfo("Info", "Select order type")
            return
        
        if int(self.view.layout.qty_var.get()) <= 0:
            messagebox.showinfo("Info", "Select quantity")
            return
        
        if int(self.view.layout.available_var) < self.total:
            messagebox.showerror("Error", "Insufficient funds")
            return
        
        result = messagebox.askokcancel("Sell order", f"You are about to sell {self.quantity} {self.view.layout.symbol} @ {self.total:.2f}$", detail="Confirm sell order?")
        
        if result:
            return self.execute_sell()
        else:
            print("Order canceled")
                
    def execute_sell(self):

        print("processing order")

        self.view.layout.sell_window.destroy()

        messagebox.showinfo("Order executed", "Your order is being processed")

        symbol = self.view.layout.symbol
        user_id = state.current_user[0]
        side = 'SELL'
        type = self.view.layout.rb_var.get()
        
        sell_order = SellOrder(user_id, symbol, side, type, self.quantity, self.price, self.total)

        sell_order.process_order()

        pages_state.pages["home"][1].frame1.layout.refresh()
        pages_state.pages["positions"][1].view.layout_frame2.refresh()
        pages_state.pages["profile"][1].view.layout_frame2.refresh()
        
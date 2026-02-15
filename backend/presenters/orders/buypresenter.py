from datetime import datetime
from tkinter import messagebox
from backend.models.orders.buy import BuyOrder
from frontend.gui.root import pages
from frontend.views.orders.buy import BuyView
from backend.db.db import db
import backend.users.state as state
import backend.states.pages as pages_state

class BuyPresenter:
    def __init__(self, root, symbol, df):
        self.view = BuyView(root, symbol, df)
        self.on_qty_change = self.on_qty_change
        self.view.layout.qty_var.trace_add("write", self.on_qty_change)
        self.on_bb_press = self.on_bb_press
        self.view.layout.buy_button.config(command=self.on_bb_press)
        self.quantity = None
        self.price = None
        self.total = None
        self.execute_buy = self.execute_buy

    def on_qty_change(self, *args):
            try:
                self.quantity = int(self.view.layout.qty_var.get())
                self.price = float(self.view.layout.df.iloc[-1]["Close"])
                self.total = self.quantity * self.price
                self.view.layout.total_var.set(f"Total: {self.total:.2f}$")
            except ValueError:
                self.view.layout.total_var.set("Total: -")

    def on_bb_press(self):
        if self.view.layout.rb_var.get() != "MARKET":
            messagebox.showinfo("Info", "Select order type")
            return
        
        if int(self.view.layout.qty_var.get()) <= 0:
            messagebox.showinfo("Info", "Select quantity")
            return
        
        if int(self.view.layout.available_var) < self.total:
            messagebox.showerror("Error", "Insufficient funds")
            return
        
        result = messagebox.askokcancel("Buy order", f"You are about to buy {self.quantity} {self.view.layout.symbol} @ {self.total:.2f}$", detail="Confirm buy order?")
        if result:
            return self.execute_buy()
        else:
            print("Order canceled")
                
    def execute_buy(self):

        print("processing order")

        self.view.layout.buy_window.destroy()

        messagebox.showinfo("Order executed", "Your order is being processed")

        symbol = self.view.layout.symbol
        user_id = state.current_user[0]
        side = 'BUY'
        type = self.view.layout.rb_var.get()
        
        buy_order = BuyOrder(user_id, symbol, side, type, self.quantity, self.price, self.total)

        buy_order.process_order()

        pages_state.pages["home"][1].frame1.layout.refresh()
        pages_state.pages["positions"][1].view.layout_frame2.refresh()
        pages_state.pages["profile"][1].view.layout_frame2.refresh()
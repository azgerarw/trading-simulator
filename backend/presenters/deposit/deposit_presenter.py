from tkinter import messagebox
from backend.models.deposits.deposit import Deposit
from backend.models.deposits.types import Types
from frontend.gui.root import pages
from frontend.views.deposit.view import View
import backend.users.state as state
import backend.states.pages as pages_state

class DepositPresenter:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.view = View(container=self.container, root=self.root, pages=self.pages)
        self.types = Types()
        self.view.layout_frame1.navbar.on_select = self.on_selected_option
        
        self.view.layout_frame2.on_filter_selected = self.check
        self.view.layout_frame2.confirm_deposit = self.deposit

        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.container.rowconfigure(1, weight=20)

    def on_selected_option(self, value):

        self.view.layout_frame1.navbar.check_option(value, self.pages)

    def check(self, value):
        if value == "bank_transfer":
            self.view.layout_frame2.reference.set(f"Reference: USER_{state.current_user[0]}")
            self.view.layout_frame2.bank_transfer_frame.tkraise()
        else:
            self.view.layout_frame2.card_frame.tkraise()
    
    def deposit(self):

        card_number = self.view.layout_frame2.number_entry.get()
        cvv = self.view.layout_frame2.cvv_entry.get()
        amount = self.view.layout_frame2.card_amount_entry.get()
        card_circuit = self.view.layout_frame2.filter_var2.get()
        
        if not amount:
            messagebox.showwarning("error", "enter valid amount to deposit")
            return

        if not card_number:
            messagebox.showwarning("error", "card number missing")
            return

        if not card_circuit:
            messagebox.showwarning("error", "select bank services provider")
            return

        if not cvv:
            messagebox.showwarning("error", "cvv number missing")
            return

        if len((cvv)) != 3:
            messagebox.showwarning("error", "invalid cvv")
            return
        

        deposit = Deposit(amount=amount, type="CARD")
        deposit.create()

        messagebox.showinfo("deposit", "deposit processed", detail="funds will be credited within 2 working days")

        self.view.layout_frame2.cover.tkraise()

        pages_state.pages["positions"][1].view.layout_frame2.refresh()
        pages_state.pages["profile"][1].view.layout_frame2.refresh()
        self.view.layout_frame1.refresh()

    
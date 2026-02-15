from tkinter import END, messagebox
from frontend.gui.root import pages
from frontend.views.withdraw.view import View
import backend.users.state as state
from backend.models.withdrawals.withdraw import Withdraw
import backend.states.pages as pages_state

class WithdrawPresenter:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.view = View(container=self.container, root=self.root, pages=self.pages)
        self.view.layout_frame1.navbar.on_select = self.on_selected_option
        self.view.layout_frame2.on_filter_selected = self.check

        self.view.layout_frame2.confirm_withdraw = self.withdraw

        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.container.rowconfigure(1, weight=20)

    def on_selected_option(self, value):

        self.view.layout_frame1.navbar.check_option(value, self.pages)

    def check(self, value):
        if value == "International":
            self.view.layout_frame2.filter_var2.set(value)
            self.view.layout_frame2.swift_label.grid()
            self.view.layout_frame2.swift_entry.grid()
        else:
            self.view.layout_frame2.filter_var2.set(value)
            self.view.layout_frame2.swift_label.grid_remove()
            self.view.layout_frame2.swift_entry.grid_remove()

    def withdraw(self):

        amount = self.view.layout_frame2.amount_entry.get()
        beneficiary = self.view.layout_frame2.user_name_entry.get()
        bank = self.view.layout_frame2.bank_entry.get()
        iban = self.view.layout_frame2.iban_entry.get()
        type = self.view.layout_frame2.filter_var2.get()
        swift = self.view.layout_frame2.swift_entry.get()
        print(state.user_wallet[5])
        if not beneficiary:
            messagebox.showwarning("error", "beneficiary name missing")
            return

        if not iban:
            messagebox.showwarning("error", "iban missing")
            return
        
        if not bank:
            messagebox.showwarning("error", "bank name missing")
            return

        if not amount:
            messagebox.showwarning("error", "enter valid amount to withdraw")
        else:
            if int(amount) > state.user_wallet[4]:
                messagebox.showwarning("error", "amount to be withdrawed must be lower than your account balance")
                return
        
        if not type:
            messagebox.showwarning("error", "select bank transfer type")
        else:
            if type == 'International' and not swift:
                messagebox.showwarning("error", "enter swift code")
                return
        

        withdrawal = Withdraw(amount=amount)
        withdrawal.create()

        messagebox.showinfo("withdrawal", "withdrawal processed", detail="funds will be credited within 2 working days")

        self.view.layout_frame2.amount_entry.delete(0, END)
        self.view.layout_frame2.user_name_entry.delete(0, END)
        self.view.layout_frame2.bank_entry.delete(0, END)
        self.view.layout_frame2.iban_entry.delete(0, END)

        pages_state.pages["profile"][1].view.layout_frame2.refresh()
        self.view.layout_frame1.refresh()

    
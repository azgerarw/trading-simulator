from backend.models.deposits.types import Types
from backend.models.svmodels.symbol_component import SymbolData
import backend.users.state as state
from tkinter import ttk
from tkinter import *
from frontend.gui.symbol.symbol import open_symbol_window
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

class Layout2:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.frame_1 = None
        self.on_logout = None
        self.menu = None
        self.var = StringVar(value="Menu")
        self.values = ["Menu", "Home", "Positions", "Deposit", "Withdraw", "Profile", "Logout"]
        self.frame2 = None
        self.types = Types()
        self.filter_var = StringVar(value="")
        self.filter_var2 = StringVar(value="")
        self.bank_transfer_frame = None
        self.confirm_withdraw = None

    def build(self):
        
        self.frame2 = Frame(self.container, width=900, height=900, pady=20, padx=20, bg="red")
        self.frame2.grid(row=1,column=0, sticky="n")

        self.bank_transfer_frame = ttk.Labelframe(self.frame2, width=700, height=500, padding=15, bootstyle="primary", text="Enter bank account details: ")
        self.bank_transfer_frame.grid(row=0, column=0, sticky="n")
        self.bank_transfer_frame.grid_propagate(False)
        self.bank_transfer_frame.columnconfigure(0, weight=1)
        self.bank_transfer_frame.columnconfigure(1, weight=1)

        for row in range(7):
            self.bank_transfer_frame.rowconfigure(row, weight=1)

        for col, option in enumerate(["SEPA", "International"]):
            rb = ttk.Radiobutton(
                self.bank_transfer_frame,
                text=option,
                variable=self.filter_var2,
                value=option,
                bootstyle="primary",
                command=lambda opt=option: (
                    self.on_filter_selected(opt)
                )
            )
            rb.grid(row=8, column=col, padx=4, pady=4, sticky="n")

        user_name_label = ttk.Label(self.bank_transfer_frame, text="Beneficiary:")
        user_name_label.grid(row=0, column=0, sticky="n", columnspan=2)

        self.user_name_entry = ttk.Entry(self.bank_transfer_frame)
        self.user_name_entry.grid(row=1, column=0, sticky='n', columnspan=2)

        iban_label = ttk.Label(self.bank_transfer_frame, text="IBAN:")
        iban_label.grid(row=2, column=0, sticky="n", columnspan=2)

        self.iban_entry = ttk.Entry(self.bank_transfer_frame)
        self.iban_entry.grid(row=3, column=0, sticky='n', columnspan=2)

        bank_label = ttk.Label(self.bank_transfer_frame, text="Bank: ")
        bank_label.grid(row=4, column=0, sticky='n', columnspan=2)

        self.bank_entry = ttk.Entry(self.bank_transfer_frame)
        self.bank_entry.grid(row=5, column=0, sticky='n', columnspan=2)

        amount_label = ttk.Label(self.bank_transfer_frame, text='Amount: ')
        amount_label.grid(row=6, column=0, sticky='n', columnspan=2)

        self.amount_entry = ttk.Entry(self.bank_transfer_frame)
        self.amount_entry.grid(row=7, column=0, sticky='n', columnspan=2)

        self.swift_label = ttk.Label(self.bank_transfer_frame, text="SWIFT:")
        self.swift_label.grid(row=9, column=0, sticky="n", columnspan=2)
        self.swift_label.grid_remove()

        self.swift_entry = ttk.Entry(self.bank_transfer_frame)
        self.swift_entry.grid(row=10, column=0, sticky='n', columnspan=2)
        self.swift_entry.grid_remove()

        message2_label = ttk.Label(self.bank_transfer_frame, text="Funds are credited within 1–2 business days")
        message2_label.grid(row=11, column=0, sticky="n", columnspan=2)

        withdraw_button = ttk.Button(self.bank_transfer_frame, text='Confirm', bootstyle='primary', command=lambda: self.confirm_withdraw())
        withdraw_button.grid(row=12, column=0, sticky='ew', columnspan=2)

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
        self.on_filter_selected = None
        self.on_card_filter_selected = None
        self.bank_transfer_frame = None
        self.card_frame = None
        self.card_amount_entry = None
        self.cvv_entry = None
        self.number_entry = None
        self.cover = None
        self.on_bt_check = None
        self.confirm_deposit = None
        self.reference = StringVar()

    def build(self):
        
        self.frame2 = Frame(self.container, width=900, height=900, pady=20, padx=20, bg="red")
        self.frame2.grid(row=1,column=0, sticky="n")

        deposit_frame = ttk.Labelframe(self.frame2, width=700, height=500, padding=5, bootstyle="primary", text="Select method")
        deposit_frame.grid(row=0, column=0, sticky="n")
        deposit_frame.grid_propagate(False)
        deposit_frame.columnconfigure(0, weight=1)

        rb_frame = ttk.Frame(deposit_frame)
        rb_frame.grid(row=0, column=0, sticky="n")

        for col, option in enumerate(self.types.types):
            rb = ttk.Radiobutton(
                rb_frame,
                text=option,
                variable=self.filter_var,
                value=option,
                bootstyle="primary",
                command=lambda opt=option: (
                    self.on_filter_selected and self.on_filter_selected(opt)
                )
            )
            rb.grid(row=0, column=col, padx=4, pady=4)
            rb.columnconfigure(col, weight=1)

        self.bank_transfer_frame = ttk.Labelframe(deposit_frame, height=420, width=650, text="Send a bank transfer to: ", padding=10)
        self.bank_transfer_frame.grid(row=1, column=0)
        self.bank_transfer_frame.grid_propagate(False)
        self.bank_transfer_frame.columnconfigure(0, weight=1)

        for row in range(7):
            self.bank_transfer_frame.rowconfigure(row, weight=1)

        broker_label = ttk.Label(self.bank_transfer_frame, text="Beneficiary: MyBroker Europe Ltd")
        broker_label.grid(row=0, column=0, sticky="n")

        iban_label = ttk.Label(self.bank_transfer_frame, text="IBAN: IT0000000000000000000000000")
        iban_label.grid(row=2, column=0, sticky="n")

        bic_label = ttk.Label(self.bank_transfer_frame, text="BIC: XXXXXXXXXXX")
        bic_label.grid(row=3, column=0, sticky="n")

        user_label = ttk.Label(self.bank_transfer_frame, textvariable=self.reference)
        user_label.grid(row=4, column=0, sticky="n")
        
        message1_label = ttk.Label(self.bank_transfer_frame, text="When bank transfer has been made, send the certificate to us via email at xxxxxx@xxxxx.xx")
        message1_label.grid(row=6, column=0, sticky="n")

        message2_label = ttk.Label(self.bank_transfer_frame, text="Funds are credited within 1–2 business days")
        message2_label.grid(row=7, column=0, sticky="n")

        




        self.card_frame = ttk.Labelframe(deposit_frame, height=420, width=650, text="fill the form with your card details", padding=10)
        self.card_frame.grid(row=1, column=0)
        self.card_frame.grid_propagate(False)

        self.card_frame.columnconfigure(0, weight=1)
        self.card_frame.columnconfigure(1, weight=1)

        for row in range(8):
            self.card_frame.rowconfigure(row, weight=1)

        for col, option in enumerate(["Visa", "Mastercard"]):
            rb = ttk.Radiobutton(
                self.card_frame,
                text=option,
                variable=self.filter_var2,
                value=option,
                bootstyle="primary"
            )
            rb.grid(row=5, column=col, padx=4, pady=4, sticky="n")
            rb.columnconfigure(col, weight=1)

        circuit_label = ttk.Label(self.card_frame, text="Select circuit")
        circuit_label.grid(row=4, column=0, sticky="n", columnspan=2)

        card_amount_label = ttk.Label(self.card_frame, text="Amount")
        card_amount_label.grid(row=0, column=0, sticky="n", columnspan=2)

        self.card_amount_entry = ttk.Entry(self.card_frame, bootstyle="primary")
        self.card_amount_entry.grid(row=1, column=0, sticky="n", columnspan=2)

        card_number_label = ttk.Label(self.card_frame, text="Card number")
        card_number_label.grid(row=2, column=0, columnspan=2, sticky="n")

        self.number_entry = ttk.Entry(self.card_frame, bootstyle="primary")
        self.number_entry.grid(row=3, column=0, columnspan=2, sticky="n")

        cvv_label = ttk.Label(self.card_frame, text="CVV")
        cvv_label.grid(row=6, column=0, columnspan=2, sticky="n")

        self.cvv_entry = ttk.Entry(self.card_frame, bootstyle="primary")
        self.cvv_entry.grid(row=7, column=0, columnspan=2, sticky="n")

        card_button = ttk.Button(self.card_frame, text="Confirm", bootstyle="primary", command=lambda: self.confirm_deposit())
        card_button.grid(row=8, column=0, sticky="ew", columnspan=2)



        self.cover = Frame(deposit_frame, height=420, width=650, pady=10, padx=10)
        self.cover.grid(row=1, column=0)
        self.cover.grid_propagate(False)
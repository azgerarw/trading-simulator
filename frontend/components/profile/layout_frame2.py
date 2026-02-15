from backend.models.profile.user_history.types import Types
from backend.models.svmodels.symbol_component import SymbolData
from backend.models.users.user import User
import backend.users.state as state
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
from PIL import Image, ImageTk

class Layout2:
    def __init__(self, container, root, pages):
        self.container = container
        self.root = root
        self.pages = pages
        self.frame_1 = None
        self.frame2 = None
        self.frame2_personal_info = None
        self.frame2_operations = None
        self.avatar = None
        self.name = None
        self.lastname = None
        self.email = None
        self.birthday = None
        self.creation_date = None
        self.db = None
        self.balance = None
        self.types = Types()
        self.filter_var = StringVar(value="")
        self.trades_frame = None
        self.deposits_frame = None
        self.withdrawals_frame = None
        self.ab = state.user_wallet[4] if state.user_wallet else ''
        self.delete_account = None

    def build(self):
        
        self.frame2 = Frame(self.container, height=500, width=950, padx=10, pady=10)
        self.frame2.grid(row=1, column=0)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.frame2_personal_info = ttk.Labelframe(self.frame2, text=f'USER #{state.current_user[0] if state.current_user else ''}' ,height=480, width=300, padding=5, bootstyle='primary')
        self.frame2_personal_info.grid(row=0, column=1, sticky="nsew")

        for r in range(6):
            if r == 0:
                self.frame2_personal_info.rowconfigure(r, weight=5)
            else:
                self.frame2_personal_info.rowconfigure(r, weight=1)

        pdh = Label(self.frame2_personal_info, text=f'Personal details', anchor='center', padx=5, pady=5)
        pdh.grid(row=1, column=0)

        self.name = Label(self.frame2_personal_info, text=f'Name: ', anchor='w', padx=2, pady=2)
        self.name.grid(row=2, column=0, sticky='ew')

        self.lastname = Label(self.frame2_personal_info, text=f'Lastname: ', anchor='w', padx=2, pady=2)
        self.lastname.grid(row=3, column=0, sticky='ew')

        self.email = Label(self.frame2_personal_info, text=f'Email address: ', anchor='w', padx=2, pady=2)
        self.email.grid(row=4, column=0, sticky='ew')

        self.birthdate = Label(self.frame2_personal_info, text=f'Birthdate: ', anchor='w', padx=2, pady=2)
        self.birthdate.grid(row=5, column=0, sticky='ew')

        self.creation_date = Label(self.frame2_personal_info, text=f'Account created on: ', anchor='w', padx=2, pady=2)
        self.creation_date.grid(row=6, column=0, sticky='ew')

        self.db = ttk.Button(self.frame2_personal_info, text=f'Delete Account', bootstyle="primary", command=lambda: self.delete_account())
        self.db.grid(row=7, column=0, sticky='ew')


        self.frame2_operations = ttk.Labelframe(self.frame2, text=f'USER HISTORY', height=480, width=600, padding=10, bootstyle='primary')
        self.frame2_operations.grid(row=0, column=0, sticky="nsew")
        self.frame2_operations.grid_propagate(False)

        for r in range(2):

            if r == 2:
                self.frame2_operations.rowconfigure(r, weight=10)
            else:
                self.frame2_operations.rowconfigure(r, weight=1)

        self.frame2_operations.columnconfigure(0, weight=1)
        
        self.balance = Label(self.frame2_operations, text=f"Balance: {self.ab}", anchor='center', padx=10, pady=10)
        self.balance.grid(row=0, column=0, sticky="ew")

        rb_frame = ttk.Frame(self.frame2_operations, padding=10)
        rb_frame.grid(row=1, column=0, sticky="ew")

        for r in range(3):
            rb_frame.columnconfigure(r, weight=1)

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
            rb.grid(row=0, column=col, padx=4, pady=4, sticky="n")


        self.trades_frame = ttk.Labelframe(self.frame2_operations, text='Trades history', height=350, width=500, padding=5)
        self.trades_frame.grid(row=2, column=0)
        self.trades_frame.grid_propagate(False)

        self.trades_scrollbar = Scrollbar(self.trades_frame, orient="vertical")
        self.trades_scrollbar.grid(row=0, column=1, sticky="ns")

        self.trades_canvas = Canvas(
            self.trades_frame,
            height=350,
            width=500,
            bg="#fafafa",
            yscrollcommand=self.trades_scrollbar.set
        )
        self.trades_canvas.grid(row=0, column=0, sticky="nsew")

        self.trades_scrollbar.config(command=self.trades_canvas.yview)

        self.trades_frame.rowconfigure(0, weight=1)
        self.trades_frame.columnconfigure(0, weight=1)

        self.trades_container = Frame(self.trades_canvas, bg="#fafafa", padx=10, pady=10)

        self.trades_canvas_window = self.trades_canvas.create_window(
            (0, 0),
            window=self.trades_container,
            anchor="nw"
        )

        def _on_trades_frame_configure(event):
            self.trades_canvas.configure(
                scrollregion=self.trades_canvas.bbox("all")
            )

        self.trades_container.bind("<Configure>", _on_trades_frame_configure)




        self.deposits_frame = ttk.Labelframe(self.frame2_operations, text='Deposits history', height=350, width=500, padding=10)
        self.deposits_frame.grid(row=2, column=0)
        self.deposits_frame.grid_propagate(False)

        self.deposits_scrollbar = Scrollbar(self.deposits_frame, orient="vertical")
        self.deposits_scrollbar.grid(row=0, column=1, sticky="ns")

        self.deposits_canvas = Canvas(
            self.deposits_frame,
            height=350,
            width=500,
            bg="#fafafa",
            yscrollcommand=self.deposits_scrollbar.set
        )
        self.deposits_canvas.grid(row=0, column=0, sticky="nsew")

        self.deposits_scrollbar.config(command=self.deposits_canvas.yview)

        self.deposits_frame.rowconfigure(0, weight=1)
        self.deposits_frame.columnconfigure(0, weight=1)

        self.deposits_container = Frame(self.deposits_canvas, bg="#fafafa", padx=10, pady=10)

        self.deposits_canvas_window = self.deposits_canvas.create_window(
            (0, 0),
            window=self.deposits_container,
            anchor="nw"
        )

        def _on_deposits_frame_configure(event):
            self.deposits_canvas.configure(
                scrollregion=self.deposits_canvas.bbox("all")
            )

        self.deposits_container.bind("<Configure>", _on_deposits_frame_configure)




        self.withdrawals_frame = ttk.Labelframe(self.frame2_operations, text='Withdrawals history', height=350, width=500, padding=10)
        self.withdrawals_frame.grid(row=2, column=0)
        self.withdrawals_frame.grid_propagate(False)

        self.withdrawals_scrollbar = Scrollbar(self.withdrawals_frame, orient="vertical")
        self.withdrawals_scrollbar.grid(row=0, column=1, sticky="ns")

        self.withdrawals_canvas = Canvas(
            self.withdrawals_frame,
            height=350,
            width=500,
            bg="#fafafa",
            yscrollcommand=self.withdrawals_scrollbar.set
        )
        self.withdrawals_canvas.grid(row=0, column=0, sticky="nsew")

        self.withdrawals_scrollbar.config(command=self.withdrawals_canvas.yview)

        self.withdrawals_frame.rowconfigure(0, weight=1)
        self.withdrawals_frame.columnconfigure(0, weight=1)

        self.withdrawals_container = Frame(self.withdrawals_canvas, bg="#fafafa", padx=10, pady=10)

        self.withdrawals_canvas_window = self.withdrawals_canvas.create_window(
            (0, 0),
            window=self.withdrawals_container,
            anchor="nw"
        )

        def _on_withdrawals_frame_configure(event):
            self.withdrawals_canvas.configure(
                scrollregion=self.withdrawals_canvas.bbox("all")
            )

        self.withdrawals_container.bind("<Configure>", _on_withdrawals_frame_configure)

        self.cover = ttk.Frame(self.frame2_operations, height=350, width=500, padding=10)
        self.cover.grid(row=2, column=0)
        self.cover.grid_propagate(False)

        
    def refresh(self):
        if not state.current_user:
            return

        self.wallet = User().fetch_wallet(state.current_user[0], 'USD')

        self.name.config(text=f"Name: {state.current_user[2]}")
        self.lastname.config(text=f"Lastname: {state.current_user[3]}")
        self.email.config(text=f"Email: {state.current_user[1]}")
        self.birthdate.config(text=f"Birthdate: {state.current_user[4]}")
        self.balance.config(text=f"Balance: {self.wallet[4]:.2f}")
        self.creation_date.config(text=f'Account created on: {state.current_user[5]}')

        if state.current_user[7]:
            img = Image.open(state.current_user[7]).resize((200,200))
            photo = ImageTk.PhotoImage(img) 

            self.avatar = Label(self.frame2_personal_info, image=photo)
            self.avatar.image = photo
            self.avatar.grid(row=0, column=0, sticky='nsew')
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import DateEntry # type: ignore
import re
from backend.users.create import create_account

import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

def open_top_window(root):
        create_account_window = Toplevel(root, padx=15, pady=15, background="white")
        create_account_window.title("Create account")

        for row in range(15):

                create_account_window.rowconfigure(row, weight=1)                

        fields = {
                "name": {
                "label": "Name",
                "regex": r"^[A-Za-z]{2,}$",
                "error": "Name must be at least 2 characters long"
                },
                "lastname": {
                "label": "Lastname",
                "regex": r"^[A-Za-z]{2,}$",
                "error": "Lastname is too short"
                },
                "email": {
                "label": "Email",
                "regex": r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",
                "error": "Invalid email"
                },
                "password": {
                "label": "Password",
                "regex": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$",
                "error": "Password must include at least 1 cap letter, 1 lowercase letter, 1 number and 1 special character"
                }
        }
        
        widgets = {}

        def validate(field_key, value):
                field = fields[field_key]

                if re.match(field["regex"], value):
                        widgets[field_key]["var"].set(field["label"])
                        widgets[field_key]["entry"].config(fg="green")
                else:
                        widgets[field_key]["var"].set(field["error"])
                        widgets[field_key]["entry"].config(fg="red")
                return True

        row = 1
        for key, info in fields.items():
                var = StringVar(value=info["label"])
                
                label = Label(create_account_window, textvariable=var, background="white", anchor='w', width=25, pady=10)
                label.grid(row=row, column=0, columnspan=2)
                row += 1

                vcmd = create_account_window.register(lambda value, k=key: validate(k, value))

                entry = Entry(
                create_account_window, width=25,
                validate="key",
                validatecommand=(vcmd, "%P")
                )
                entry.grid(row=row, column=0, columnspan=2)
                row += 1

                widgets[key] = {
                "var": var,
                "entry": entry
                }

        widgets["password"]["entry"].config(show="*")
        
        cal_label = Label(create_account_window, text="Birthdate", width=25, anchor='w', background="white", pady=10).grid(row=9, column=0, columnspan=2)
        cal_entry = ttk.DateEntry(create_account_window, width=25)
        cal_entry.grid(row=10, column=0, columnspan=2)

        checkbutton_frame = Frame(create_account_window)
        checkbutton_frame.grid(row=11, column=0, columnspan=2)
        checkbutton_label = Label(checkbutton_frame, background="white", text='I accept terms and conditions', pady=10).grid(row=0, column=1)
        cb_var = BooleanVar()
        checkbutton = Checkbutton(checkbutton_frame, background="white", activebackground='white', variable=cb_var)
        checkbutton.grid(row=0, column=0)

        file_path = StringVar() 

        def select_img():
                fp = filedialog.askopenfilename(
                title="Select profile picture",
                filetypes=[
                ("Image files", "*.png *.jpg *.jpeg"),
                ("All files", "*.*")
                ])

                file_path.set(fp)
        
        avatar_label = Label(create_account_window, text="Avatar", pady=10)
        avatar_label.grid(row=12, column=0)

        entry = ttk.Entry(create_account_window, textvariable=file_path, width=10)
        entry.grid(row=13, column=0)

        button = ttk.Button(create_account_window, text="Browse", bootstyle="primary", command=select_img)
        button.grid(row=13, column=1)

        create_button_padding = Label(create_account_window, text="", pady=10).grid(row=14, column=0, columnspan=2)

        create = Button(create_account_window, width=25, text="Create", justify="center", background="red", activebackground="orange", command=lambda:
                        create_account(create_account_window, widgets["name"]["entry"].get(), widgets["lastname"]["entry"].get(), widgets["email"]["entry"].get(), cal_entry.entry.get(), widgets["password"]["entry"].get(), cb_var.get(), fields, file_path.get()))
        create.grid(row=15, column=0, columnspan=2)

        
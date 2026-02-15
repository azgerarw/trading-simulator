from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import DateEntry # type: ignore
import re
from backend.users.changepassword import change_password

import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

def open_cp_window(root):
        
        change_password_window = Toplevel(root, padx=15, pady=15, background="white")
        change_password_window.title("Change password")

        for i in range(8):
            change_password_window.rowconfigure(i, weight=1)

        email_label = Label(change_password_window, text='Email', anchor='w', pady=10, padx=10)
        email_label.grid(row=1, column=0)

        input_email = Entry(change_password_window, width=25, border=1, justify="left")
        input_email.grid(row=2, column=0)

        op_label = Label(change_password_window, text='Old password', anchor='w', pady=10, padx=10)
        op_label.grid(row=3, column=0)

        old_password = Entry(change_password_window, width=25, border=1, justify="left", show="*")
        old_password.grid(row=4, column=0)

        np_label = Label(change_password_window, text='New password', anchor='w', pady=10, padx=10)
        np_label.grid(row=5, column=0)

        new_password = Entry(change_password_window, width=25, border=1, justify="left", show="*")
        new_password.grid(row=6, column=0)

        gap_label = Label(change_password_window, text='', anchor='w', pady=10, padx=10)
        gap_label.grid(row=7, column=0)

        change_password_button = ttk.Button(change_password_window, text='Confirm', command=lambda e=input_email, op=old_password, np=new_password, w=change_password_window: change_password(e,op,np,w))
        change_password_button.grid(row=8, column=0, sticky='ew')



        
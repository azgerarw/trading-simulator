
from tkinter import *
from tkinter import messagebox
import re

from backend.models.users.user import User

def create_account(window, name, lastname, email, birthdate, password, tc, fields, file_path):
    
    if tc == True:

        labels = ("name", "lastname", "email", "password")
        values = (name, lastname, email, password)

        for index, value in enumerate(values, start=0):
            key = labels[index]
            item = fields[key]

            if not value:
                messagebox.showerror("Form error", f"{item['label']} field is mandatory")
                print(f"{item['label']} field is mandatory")
                return

            if not re.match(item["regex"], value):
                messagebox.showerror("Form error", item["error"])
                print(f"{item["error"]}")
                return

            print(f"{key} is ok")

        print("All fields validated correctly!")

        new_user = User()

        new_user.create(name, lastname, email, birthdate, password, file_path)
        
        messagebox.showinfo("New account", "Your account has been created")
        
        window.destroy()
    else:
        messagebox.showerror("T&C", "You must accept T&C")

    
from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt
from datetime import datetime, date, time, timezone
from backend.db.db import db
import backend.users.state as state

def login(email_entry, password_entry, pages=None):
    global current_user

    email = email_entry.get()
    password = password_entry.get()

    rows = db.execute("SELECT * FROM users WHERE email = ?", [email])
    
    user = rows.fetchone()

    wallet = db.execute("SELECT * FROM wallets WHERE user_id = ? AND asset = ?", [user[0], "USD"])

    user_wallet = wallet.fetchone()
    if not user:
        messagebox.showerror("Login", "User not found")
        return

    stored_hash = user[6]

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        current_user = user
        print("Login successful!")
        state.current_user = current_user
        state.user_wallet = user_wallet
        pages["home"][1].frame1.layout.build(pages["home"][0])
        pages["profile"][1].view.layout_frame2.refresh()
        pages["positions"][1].view.layout_frame2.refresh()
        pages["home"][0].tkraise()
    else:
        messagebox.showerror("Login", "Wrong password!")
        print("Wrong password!")

    
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    


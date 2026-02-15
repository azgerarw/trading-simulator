from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt
from datetime import datetime, date, time, timezone
from backend.db.db import db
from backend.models.users.user import User
import backend.users.state as state

def change_password(email_entry, op_entry, np_entry, window):
    global current_user

    email = email_entry.get()
    op = op_entry.get()
    np = np_entry.get()

    user = User()
    user.update(email, op, np)

    email_entry.delete(0, END)
    op_entry.delete(0, END)
    np_entry.delete(0, END)

    window.destroy()
    


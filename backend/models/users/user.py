from pathlib import Path
import re
import shutil
import sqlite3
from tkinter import messagebox
import bcrypt
from datetime import datetime, date, time, timezone
from backend.db.db import db

class User:
    def __init__(self):
        pass

    def create(self, name, lastname, email, birthdate, password, file_path):
        hashed = bcrypt.hashpw(bytes(password.encode("utf-8")), bcrypt.gensalt())
        timestamp = datetime.now()
        balance = 5000
        asset = "USD"
        db.execute("INSERT INTO users (email, name, lastname, birthdate, timestamp, password) VALUES (?,?,?,?,?,?)", [email, name, lastname, birthdate, timestamp, hashed])
        
        user_rows = db.execute("SELECT * FROM users WHERE email = ?", [email])
    
        user = user_rows.fetchone()

        user_id = user[0]

        if file_path:

            (Path.cwd() / "backend" / "users" / "avatars" / f"user_{user_id}" ).mkdir(parents=True)

            avatars = Path.cwd().joinpath('backend/users/avatars/').joinpath(f"user_{user_id}")

            user_avatar = shutil.copy(file_path, avatars)

            db.execute("UPDATE users SET avatar = ? WHERE user_id = ?", [str(user_avatar), user_id])

        db.execute("INSERT INTO wallets (user_id, asset, balance, available_balance, updated_at) VALUES (?,?,?,?,?)", [user_id, asset, balance, balance, timestamp])

        db.connection.commit()

        return
    
    def update(self, email, password, newpassword):

        password_regex = { 
            "regex": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$",
            "error": "Password must include at least 1 cap letter, 1 lowercase letter, 1 number and 1 special character"
        }
        user = db.execute('SELECT * FROM users WHERE email = ?', [email]).fetchone()

        if not user:
            messagebox.showerror("Login", "User not found")
            return

        stored_hash = user[6]

        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            
            if re.match(password_regex['regex'], newpassword):
                hashed = bcrypt.hashpw(bytes(newpassword.encode("utf-8")), bcrypt.gensalt())
            else:
                messagebox.showerror("Error", f"{password_regex['error']}")

            result = messagebox.askokcancel("Password change", "Confirm to change password")
                
            if result:

                db.execute('UPDATE users SET password = ? WHERE email = ?', [hashed, email])

                db.connection.commit()

                messagebox.showinfo("Password", "Password updated!")

    def delete(self, user_id):
        
        db.execute("PRAGMA foreign_keys = ON")

        db.execute('DELETE FROM users WHERE user_id = ?', [user_id])

        db.connection.commit()

    def fetch(self, user_id):

        rows = db.execute("SELECT * FROM users WHERE user_id = ?", [user_id])
    
        user = rows.fetchone()
        
        return user
    
    def fetch_wallet(self, user_id, symbol):

        wallet = db.execute("SELECT * FROM wallets WHERE user_id = ? AND asset = ?", [user_id, symbol]).fetchone()

        return wallet

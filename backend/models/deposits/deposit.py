from backend.db.db import db
import backend.users.state as state
from datetime import datetime

class Deposit:
    def __init__(self, amount, type):
        self.user_id = state.current_user[0] if state.current_user else ""
        self.amount = amount
        self.timestamp = datetime.now()
        self.type = type
        

    def create(self):
        
        db.execute("PRAGMA foreign_keys = ON;")

        db.execute("INSERT INTO deposits (user_id, amount, type, created_at, executed_at) VALUES (?,?,?,?,?)", 
        [self.user_id, self.amount, self.type, self.timestamp, self.timestamp])

        db.execute(
            """
            UPDATE wallets
            SET balance = balance + ?,
                available_balance = available_balance + ?,
                updated_at = ?
            WHERE user_id = ? AND asset = 'USD'
            """,
            [self.amount, self.amount, self.timestamp, self.user_id]
        )

        db.connection.commit()

        return


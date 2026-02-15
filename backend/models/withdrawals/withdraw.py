from backend.db.db import db
import backend.users.state as state
from datetime import datetime

class Withdraw:
    def __init__(self, amount):
        self.user_id = state.current_user[0] if state.current_user else ""
        self.amount = amount
        self.timestamp = datetime.now()

    def create(self):
        
        db.execute("PRAGMA foreign_keys = ON;")

        db.execute("INSERT INTO withdrawals (amount, user_id, executed_on) VALUES (?,?,?)", 
        [self.amount, self.user_id, self.timestamp])

        db.execute(
            """
            UPDATE wallets
            SET balance = balance - ?,
                available_balance = available_balance - ?,
                updated_at = ?
            WHERE user_id = ? AND asset = 'USD'
            """,
            [self.amount, self.amount, self.timestamp, self.user_id]
        )

        db.connection.commit()

        return


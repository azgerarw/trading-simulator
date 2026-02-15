from backend.db.db import db
import backend.users.state as state

class Positions:
    def __init__(self, user):
        self.user_id = user
    
    def fetch(self):
        
        positions = db.execute("" \
        "SELECT symbol, quantity, average_price FROM positions WHERE user_id = ?", [self.user_id]).fetchall()

        return positions

    def fetch_by_symbol(self, symbol):
        
        position = db.execute("" \
        "SELECT quantity, average_price FROM positions WHERE user_id = ? AND symbol = ?", [self.user_id, symbol]).fetchone()

        return position
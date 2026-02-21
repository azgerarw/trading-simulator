from datetime import datetime
from backend.db.db import db
import backend.users.state as state

class BuyOrder:
    def __init__(self, user_id, symbol, side, type, quantity, price, total):
        self.timestamp = datetime.now()
        self.user_id = user_id
        self.symbol = symbol
        self.side = side
        self.type = type
        self.quantity = quantity
        self.price = price
        self.total = total

    def process_order(self):
        

        db.execute(
            "INSERT INTO orders (user_id, symbol, side, order_type, quantity, created_at)" \
            "VALUES (?,?,?,?,?,?)", [self.user_id, self.symbol, self.side, self.type, self.quantity, self.timestamp]
        )

        current_order = db.execute(
            "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC LIMIT 1",
            [self.user_id]
            ).fetchone()


        db.execute(
            "INSERT INTO trades (order_id, side, price, quantity, executed_at)" \
            "VALUES (?,?,?,?,?)", [current_order[0], self.side, self.price, self.quantity, self.timestamp]
        )

        position = db.execute(
                "SELECT position_id, quantity, average_price FROM positions WHERE user_id = ? AND symbol = ?",
                [self.user_id, self.symbol]
            ).fetchone()
        
        buy_qty = self.quantity

        if position is None:
            
            trade_price = self.price
            new_qty = buy_qty
            new_avg = trade_price

            db.execute(
            "INSERT INTO positions (user_id, symbol, quantity, average_price, created_at)"
            "VALUES (?,?,?,?,?)",
            [self.user_id, self.symbol, new_qty, new_avg, self.timestamp]
            )

        else:
            trade_price = self.price

            position_id, old_qty, old_avg = position

            new_qty = old_qty + buy_qty

            new_avg = (
                old_qty * old_avg +
                buy_qty * trade_price
            ) / new_qty

            db.execute(
                "UPDATE positions SET average_price = ?, quantity = ?, updated_at = ? WHERE position_id = ?",
                [new_avg, new_qty, self.timestamp, position_id]
            )
        
        db.execute(
            """
            UPDATE wallets
            SET balance = balance - ?,
                available_balance = available_balance - ?,
                updated_at = ?
            WHERE user_id = ? AND asset = 'USD'
            """,
            [self.total, self.total, self.timestamp, self.user_id]
        )

        asset_wallet = db.execute(
            """
            SELECT wallet_id, balance
            FROM wallets
            WHERE user_id = ? AND asset = ?
            """,
            [self.user_id, self.symbol]
        ).fetchone()

        if asset_wallet is None:
            db.execute(
                """
                INSERT INTO wallets (user_id, asset, balance, available_balance, updated_at)
                VALUES (?,?,?,?,?)
                """,
                [self.user_id, self.symbol, buy_qty, buy_qty, self.timestamp]
            )
        else:
            wallet_id, old_balance = asset_wallet

            db.execute(
                """
                UPDATE wallets
                SET balance = ?, available_balance = ?, updated_at = ?
                WHERE wallet_id = ?
                """,
                [old_balance + buy_qty, old_balance + buy_qty, self.timestamp, wallet_id]
            )

        db.connection.commit()

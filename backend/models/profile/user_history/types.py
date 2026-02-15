import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore
from tkinter import Label, ttk
from backend.db.db import db

class Types:
    def __init__(self):
        self.types = [
            "trades",
            "deposits",
            "withdrawals"
        ]
        self.row = 0

    def fetch_trades(self, user_id):

        trades = db.execute('SELECT t.trade_id, t.side, t.price, t.quantity, t.executed_at FROM trades t INNER JOIN orders ON t.order_id = orders.order_id WHERE user_id = ?', [user_id]).fetchall()

        return trades
    
    def fetch_deposits(self, user_id):

        deposits = db.execute('SELECT deposit_id, amount, type, executed_at FROM deposits WHERE user_id = ?', [user_id]).fetchall()

        return deposits
    
    def fetch_withdrawals(self, user_id):

        withdrawals = db.execute('SELECT withdrawal_id, amount, executed_on FROM withdrawals WHERE user_id = ?', [user_id]).fetchall()

        return withdrawals
    
    def build_trades(self, trades_frame, trades):

        for trade in trades:

            self.row = self.row + 1

            trade_card = ttk.Labelframe(trades_frame, text=f'TRADE #{trade[0]}', height=60, width=450, padding=5, bootstyle='warning')
            trade_card.grid(row=self.row, column=0)
            trade_card.grid_propagate(False)

            side_label = Label(trade_card, text=f'{trade[1]}, ')
            side_label.grid(row=0, column=0)

            price_label = Label(trade_card, text=f'{trade[2]:.2f}, ')
            price_label.grid(row=0, column=1)

            quantity_label = Label(trade_card, text=f'quantity: {trade[3]}, ')
            quantity_label.grid(row=0, column=2)

            timestamp_label = Label(trade_card, text=f'executed on {trade[4]}')
            timestamp_label.grid(row=0, column=3)
    
    def build_deposits(self, deposits_frame, deposits):

        for deposit in deposits:

            self.row = self.row + 1

            deposit_card = ttk.Labelframe(deposits_frame, text=f'Deposit #{deposit[0]}', height=60, width=450, padding=5, bootstyle='warning')
            deposit_card.grid(row=self.row, column=0)
            deposit_card.grid_propagate(False)

            type_label = Label(deposit_card, text=f'{deposit[2]}, ')
            type_label.grid(row=0, column=0)

            amount_label = Label(deposit_card, text=f'{deposit[1]}$, ')
            amount_label.grid(row=0, column=1)

            timestamp_label = Label(deposit_card, text=f'executed on: {deposit[3]}')
            timestamp_label.grid(row=0, column=2)

    def build_withdrawals(self, withdrawals_frame, withdrawals):

        for withdrawal in withdrawals:

            self.row = self.row + 1

            withdrawal_card = ttk.Labelframe(withdrawals_frame, text=f'Withdrawal #{withdrawal[0]}', height=60, width=450, padding=5, bootstyle='warning')
            withdrawal_card.grid(row=self.row, column=0)
            withdrawal_card.grid_propagate(False)

            amount_label = Label(withdrawal_card, text=f'executed on: {withdrawal[1]}$, ')
            amount_label.grid(row=0, column=1)

            timestamp_label = Label(withdrawal_card, text=f'executed on: {withdrawal[2]}')
            timestamp_label.grid(row=0, column=2)
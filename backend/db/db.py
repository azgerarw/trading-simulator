import sqlite3

con = sqlite3.connect("backend/db/db.db")
db = con.cursor()

'''
db.execute("PRAGMA foreign_keys = ON;")

db.execute("CREATE TABLE users  "
"(user_id INTEGER PRIMARY KEY AUTOINCREMENT," \
" email VARCHAR(30) NOT NULL, " \
"name TEXT(15) NOT NULL, " \
"lastname TEXT(15) NOT NULL, " \
"birthdate DATE NOT NULL, " \
"timestamp TEXT NOT NULL , " \
"password TEXT(255) NOT NULL, " \
"avatar TEXT);")

db.execute("CREATE TABLE wallets "
"(wallet_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
"user_id INTEGER NOT NULL," \
"asset TEXT NOT NULL," \
"balance INTEGER NOT NULL," \
"available_balance INTEGER NOT NULL," \
"updated_at TEXT NOT NULL," \
"FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE);")

db.execute("CREATE TABLE orders "
"(order_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
"user_id INTEGER NOT NULL," \
"symbol TEXT NOT NULL," \
"side TEXT CHECK (side IN ('BUY','SELL')) NOT NULL,"
"order_type TEXT CHECK (order_type IN ('LIMIT','MARKET')) NOT NULL,"
"quantity INTEGER NOT NULL,"
"created_at TEXT NOT NULL,"
"FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE);")

db.execute("CREATE TABLE trades "
"(trade_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
"order_id INTEGER," \
"side TEXT CHECK (side IN ('BUY','SELL')) NOT NULL,"
"price INTEGER NOT NULL,"
"quantity INTEGER NOT NULL,"
"executed_at TEXT NOT NULL,"
"FOREIGN KEY (order_id) REFERENCES orders(order_id)ON DELETE CASCADE);")

db.execute("CREATE TABLE positions "
"(position_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
"user_id INTEGER NOT NULL," \
"symbol TEXT NOT NULL," \
"quantity INTEGER NOT NULL," \
"average_price INTEGER NOT NULL," \
"created_at TEXT, " \
"updated_at TEXT," \
"FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE);")

db.execute("CREATE TABLE deposits "
"(deposit_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
"user_id INTEGER NOT NULL, " \
"amount REAL NOT NULL, " \
"type TEXT CHECK (type IN ('BANK_TRANSFER','CARD')) NOT NULL, "
"created_at DATETIME,"
"executed_at DATETIME, "
"FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE);")

db.execute("CREATE TABLE withdrawals "
"(withdrawal_id INTEGER PRIMARY KEY AUTOINCREMENT," \
"amount INTEGER NOT NULL," \
"user_id INTEGER NOT NULL," \
"executed_on TEXT NOT NULL," \
"FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE);")
'''
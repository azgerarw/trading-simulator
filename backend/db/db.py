import sqlite3

con = sqlite3.connect("backend/db/db.db")
db = con.cursor()

#db.execute("ALTER TABLE users ADD COLUMN password TEXT(255) NOT NULL")

#db.close()
#con.close()



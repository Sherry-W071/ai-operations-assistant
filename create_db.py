import sqlite3

conn = sqlite3.connect("operations.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    status TEXT,
    amount REAL,
    issue TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")
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

orders_data = [
    ("1001", "ABC Textile", "Delayed", 12000.0, "Raw material shortage"),
    ("1002", "Blue Yarn Co", "Shipped", 8500.0, "None"),
    ("1003", "Ever Wool Ltd", "Processing", 15000.0, "Machine maintenance")
]

cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?)",
    orders_data
)

conn.commit()
conn.close()

print("Orders inserted successfully.")
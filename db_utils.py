import sqlite3

DB_PATH = "operations.db"

def get_order_by_id(order_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None
    
    return {
        "order_id": row[0],
        "customer_name": row[1],
        "status": row[2],
        "amount": row[3],
        "issue": row[4]
    }

def get_customer_by_id(customer_id: str):
    conn =  sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None
    
    return {
        "customer_id": row[0],
        "customer_name": row[1],
        "industry": row[2],
        "region": row[3]
    }
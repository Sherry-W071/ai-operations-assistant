from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, AI Operations Assistant!"}

@app.get("/order/{order_id}")
def get_order(order_id: str):
    conn = sqlite3.connect("operations.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "order_id": row[0],
            "customer_name": row[1],
            "status": row[2],
            "amount": row[3],
            "issue": row[4]
        }
    else:
        return {"error": "Order not found"}
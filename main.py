from fastapi import FastAPI
import sqlite3
from db_utils import get_order_by_id, get_customer_by_id

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, AI Operations Assistant!"}

@app.get("/order/{order_id}")
def get_order(order_id: str):
    order = get_order_by_id(order_id)
    if order:
        return order
    else:
        return {"error": "Order not found"}
    
@app.get("/customer/{customer_id}")
def get_customer(customer_id: str):
    customer = get_customer_by_id(customer_id)
    if customer:
        return customer
    else:
        return {"error": "Customer not found"}
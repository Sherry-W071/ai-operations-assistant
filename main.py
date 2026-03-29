from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, AI Operations Assistant!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/hello")
def say_hello():
    return {"greeting": "Hi, this backend is working."}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message": f"Hello, {name}!"}
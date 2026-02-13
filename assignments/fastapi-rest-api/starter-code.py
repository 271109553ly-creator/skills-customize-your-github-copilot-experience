# FastAPI Starter Code

# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 你可以在此基础上继续实现学生的 CRUD 路由。

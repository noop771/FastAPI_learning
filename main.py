from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    name: str
    price: int

@app.get("/")
async def root():
    return {"status": "ok", "message": "Сервер работает"}

@app.get("/items")
async def items():
    return [{"id": 1, "name": "Хлеб"}, {"id": 2, "name": "Молоко"}]

@app.post("/items")
async def create_item(item: ItemCreate):
    return {"name": item.name, "price":  item.price}
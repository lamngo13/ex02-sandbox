from fastapi import FastAPI
from pydantic import BaseModel
#import FastAPI from

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.delete("/")
async def root():
    return {"message": "Deleted root :)"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

fake_items_db = [{"item_name": "Foo"},{"item_name": "Barr"},{"item_name": "Bazz"},]

@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
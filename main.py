from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Simple FastAPI Application",
    description="A lightweight starter API built with FastAPI and Uvicorn.",
    version="1.0.0"
)

# Pydantic model for POST requests
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root():
    """Health check / welcome endpoint."""
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Path parameter and query parameter example."""
    return {"item_id": item_id, "query_param": q}

@app.post("/items/")
def create_item(item: Item):
    """Request body validation example using Pydantic."""
    total_price = item.price + (item.tax or 0.0)
    return {
        "message": f"Item '{item.name}' created successfully!",
        "total_price": total_price,
        **item.model_dump()
    }
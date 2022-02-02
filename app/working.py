from tkinter import NONE
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


newapp = FastAPI()

@newapp.get("/")
def home():
    return {"Data": "Test"}


@newapp.get("/about")
def about():
    return {"Data": "About"}


inventory = {}

@newapp.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item.", gt=0)):
    return inventory[item_id]


@newapp.get("/get-by-name/{item_id}")
def get_item(*, item_id : int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@newapp.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": f"Item {item_id} already exists!"}

    inventory[item_id] = item
    return inventory[item_id]


@newapp.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": f"Item id {item_id} does not exist!"}

    if item.name != None:
        inventory[item_id].name = item.name 

    if item.price != None:
        inventory[item_id].price = item.price 

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@newapp.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The id of the item", gt=0)):
    if item_id not in inventory:
        return {"Error": f"Item id {item_id} does not exist!"}

    del inventory[item_id]
    return {"success", f"item {item_id} deleted!"}
    
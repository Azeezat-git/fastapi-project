from typing import Optional
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

inventory = {

     1: {
        "name": "Milk",
        "price": 15.99,
        "brand": "peak"

    }
  }

@app.get("/")
def get():
    return {"data": "welcome"}

@app.get("/{item_id}")
def get_id(item_id :int):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Item id {item_id} not present")
    else:
        return{"Success"}

#@app.get("/get-by-name")
#def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]     
    return {"not found"}
 
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id : int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


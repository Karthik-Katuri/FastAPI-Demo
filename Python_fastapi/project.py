# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:49:27 2024

@author: akash
"""
from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand : Optional[str]= None
    
class UpdateItem(BaseModel):
    name: Optional[str]= None
    price: Optional[float]= None
    brand : Optional[str]= None    
    
inventory = {
    }

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item", gt=0)):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item_by_name(*, item_id = int,name: Optional[str] = None, test = int ):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}        

@app.post("/create-item/{item_id}")
def create_item(item_id:int, item : Item):
    if item_id in inventory:
        return{"Error": "Item ID already exists."}
    
    inventory[item_id]= item
    return inventory[item_id]

@app.put("/update-id/{item_id}")
def update_item(item_id:int, item : UpdateItem):
    if item_id not in inventory:
        return{"Error": "Item ID not exists."}
    
    if item.name != None:
        inventory[item_id].name= item.name

    if item.price != None:
        inventory[item_id].price= item.price
        
    if item.brand != None:
        inventory[item_id].brand= item.brand   
    
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(... ,description ="the ID of the deleted item is")):
    if item_id not in inventory:
        return {"Error":" ID does not exists"}
    
    del inventory[item_id]
    
        
        
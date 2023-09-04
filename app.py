# FastAPI App

from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dataclasses import dataclass

app = FastAPI()

class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"

class Item(BaseModel):
    name: str
    category: Category
    price: float
    id: int
    count: int

items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=20, id=2, category=Category.CONSUMABLES)
}

@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_items_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {item_id=} not found")
    return items[item_id]


###################
# Will need:
###################
# Town Population
# Town Buildings and Revenue per building
# Random Event Calculator
# Season Modifier
# How to make usable for Bar?
# Classes :
# Building  - revenue, upkeep, population_impact, staff_needed, location
# Season (enum?) -  spring, summer, fall, winter
# seasonseverity (tuple: Season, int)
# Town: population, List[Building], location, name, ownership?,
# Portfolio: ownership, List[Buildings]
# (factory pattern? for generate revenue?

class Building:
    name: str
    revenue: float
    upkeep: float
    population_impact: float
    staff_needed: int
    location: str

class Town:
    ownership: str
    population: int
    location: str
    staff_needed: int
    buildings: list[Building]
    name: str

class Season(Enum):
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"
    WINTER = "Winter"

@dataclass
class SeasonSeverity:
    season: Season
    severity: int

class Portfolio:
    ownership: str
    buildings: list[Building]




@app.get("/generate_town_revenue")
def generate_town_revenue() -> dict[str, float]:
    return {"revenue": 10000}


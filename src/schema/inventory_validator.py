from typing import List

from pydantic import BaseModel


class Items(BaseModel):
    sku: str
    status:str

class InventoryValidator(BaseModel):
    order_id: str
    reserved_items:List[Items]
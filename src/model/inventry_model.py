from dataclasses import dataclass


@dataclass
class InventryModel:
    order_id:str
    sku:str
    status:str

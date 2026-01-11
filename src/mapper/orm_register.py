from sqlalchemy.orm import registry

from src.model.inventry_model import InventryModel
from src.model.order_model import OrderModel
from src.tables.inventry_table import inventry_tab
from src.tables.order_tables import order_table


map_registry=registry()

def run_mappers():
    map_registry.map_imperatively(OrderModel,order_table)
    map_registry.map_imperatively(InventryModel,inventry_tab)


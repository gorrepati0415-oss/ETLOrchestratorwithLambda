from src.model.order_model import OrderModel
from src.source.db_connection import SESSION_FACTORY


class OrderRepository:
    name='order'
    def __init__(self):
        self.session = SESSION_FACTORY()

    def insert(self, order: OrderModel):
        self.session.add(order)
        self.session.commit()
        return order


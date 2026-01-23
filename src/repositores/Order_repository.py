from sqlite3 import IntegrityError

from src.exceptions.all_exception import DuplicateOrderException
from src.model.order_model import OrderModel
from src.source.db_connection import SESSION_FACTORY
from src.utils.log_utils import logger


class OrderRepository:
    name='order'
    def __init__(self):
        self.session = SESSION_FACTORY()

    def insert(self, order: OrderModel):
        try:
            self.session.add(order)
            self.session.commit()
            logger.info("Order inserted successfully | order_id=%s", order.order_id)
            return order
        except IntegrityError as exc:
            self.session.rollback()

            logger.error(
                "Duplicate order detected | order_id=%s",
                order.order_id,
                exc_info=True
            )

            # 🔥 Raise your domain exception
            raise DuplicateOrderException(
                f"Order already exists: {order.order_id}"
            ) from exc



    def order_by_get_id(self,order_id):
        return self.session.query(OrderModel).filter(OrderModel.order_id==order_id).first()


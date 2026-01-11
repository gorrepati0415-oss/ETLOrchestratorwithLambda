import json
from src.framework.orchestration_abstract import EtlAbstractOrchestrator
from src.model.order_model import OrderModel
from src.repositores.Order_repository import OrderRepository
from src.schema.InputValidator import OrderBody


class OrderService(EtlAbstractOrchestrator):
    name = 'OrderPlaceEvent'
    def __init__(self):
        self.event=None
        self.order_dt=None


    def validate_data(self):
        self.data = json.loads(self.event['Records'][0]['body'])
        self.valid_data = OrderBody(order_id=self.data['order_id'], user_id=self.data['user_id'], total_amount=self.data['total_amount'],
                               payment_method=self.data['payment_method'], status=self.data['status'])


    def process_data(self):
        order_id = self.valid_data.order_id
        user_id = self.valid_data.user_id
        total_amount = self.valid_data.total_amount
        payment_method = self.valid_data.payment_method
        status = self.valid_data.status
        order_dt = OrderModel(
            order_id=order_id,
            user_id=user_id,
            payment_method=payment_method,
            status=status,
            total_amount=total_amount)
        repo = OrderRepository()
        repo.insert(order_dt)

    def send_to_sqs(self):
        print("sending order not required...")

    def process_the_event(self,event):
        self.event=event
import json
import uuid

from src.framework.orchestration_abstract import EtlAbstractOrchestrator
from src.model.order_model import OrderModel
from src.repositores.Order_repository import OrderRepository
from src.schema.InputValidator import OrderBody
from src.utils.log_utils import logger


class OrderService(EtlAbstractOrchestrator):
    name = 'OrderPlaceEvent'
    def __init__(self,service_name,description):
        self.service_name = service_name
        self.description = description
        self.service_id=str(uuid.uuid4())
        self.event=None
        self.order_dt=None

        logger.info(f'[{self.service_id}] Service Initiated ID:... {self.service_name} Service Name..   {self.description} Service Description..')


    def validate_data(self):
        logger.info(f'{self.service_id}  Received Event Data.. Started')
        self.data = json.loads(self.event['Records'][0]['body'])
        self.order_data = self.data['body']
        self.headers = self.data['header']

        self.valid_data = OrderBody(order_id= self.order_data['order_id'], user_id=self.order_data['user_id'], total_amount=self.order_data['total_amount'],
                               payment_method=self.order_data['payment_method'], status=self.order_data['status'])

        logger.info(f'{self.service_id}  Received Event Data.. Successful....')

        
    def process_data(self):
        logger.info(f'{self.service_id}  Received Event Data.. Started')
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

        logger.info(f'{self.service_id}  Received Event Data.. Successful....')
    def send_to_sqs(self):
        print("sending order not required...")

    def process_the_event(self,event):
        self.event=event
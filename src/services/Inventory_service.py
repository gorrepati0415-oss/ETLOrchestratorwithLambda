import json
from src.framework.orchestration_abstract import EtlAbstractOrchestrator
from src.model.inventry_model import InventryModel
from src.repositores.inventry_repository import InventryRepository
from src.schema.inventory_validator import InventoryValidator
import uuid

from src.utils.log_utils import logger


class InventoryService(EtlAbstractOrchestrator):
    name = 'inventoryReservedEvent'
    def __init__(self,service_name,description):
        self.service_name=service_name
        self.description=description
        self.service_id=str(uuid.uuid4())
        self.event=None
        self.inventory=None

        logger.info(f'[{self.service_name}] Service Initialized Id:{self.service_id}and Description:{self.description}')


    def validate_data(self):
        logger.info('data validation started....')
        self.data=json.loads(self.event['Records'][0]['body'])
        self.inverty_data=self.data['body']
        self.demo=InventoryValidator(order_id=self.inverty_data['order_id'],reserved_items=self.inverty_data['reserved_items'])
        logger.info('data validation completed.successful...')
    def process_data(self):
        logger.info('data processing started....')
        order_id=self.demo.order_id
        for item in self.demo.reserved_items:
            self.sku=item.sku
            self.status=item.status

        valid_input = InventryModel(order_id=order_id, sku=self.sku, status=self.status)
        Repo_data = InventryRepository()
        Repo_data.insert(valid_input)
        logger.info('data processing completed..successful...')

    def send_to_sqs(self):
        print("sending to flag demo..demos...")


    def process_the_event(self,event):
        self.event=event



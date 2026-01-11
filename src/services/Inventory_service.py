import json
from src.framework.orchestration_abstract import EtlAbstractOrchestrator
from src.model.inventry_model import InventryModel
from src.repositores.inventry_repository import InventryRepository
from src.schema.inventory_validator import InventoryValidator


class InventoryService(EtlAbstractOrchestrator):
    name = 'InventoryEvent'
    def __init__(self):
        self.event=None
        self.inventory=None

    def validate_data(self):
        self.data=self.event['Records'][0]['body']
        self.data=json.loads(self.data)
        self.data = json.loads(self.data)
        self.demo=InventoryValidator(order_id=self.data['order_id'],reserved_items=self.data['reserved_items'])

    def process_data(self):
        order_id=self.demo.order_id
        for item in self.demo.reserved_items:
            self.sku=item.sku
            self.status=item.status

        valid_input = InventryModel(order_id=order_id, sku=self.sku, status=self.status)
        Repo_data = InventryRepository()
        Repo_data.insert(valid_input)


    def send_to_sqs(self):
        print("sending to flag demo..demos...")


    def process_the_event(self,event):
        self.event=event



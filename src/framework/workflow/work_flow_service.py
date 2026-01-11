
from src.services.Inventory_service import InventoryService
from src.services.order_service import OrderService


class WorkFlowService:
    def __init__(self):
        self.service=[]

    def register_service(self,service):
        self.service.append(service)

    def get_service(self, service_name):
        for service in self.service:
            if service.name == service_name:
                print(service.name, service)
                return service

        raise Exception(f"Service {service_name} not found")


if __name__ == "__main__":

    work=WorkFlowService()

    work.register_service(InventoryService())
    work.register_service(OrderService())







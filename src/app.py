import json

from src.framework.etl_engine import Engine
from src.framework.workflow.work_flow_main import WorkFlow
from src.mapper.orm_register import run_mappers
from src.services.Inventory_service import InventoryService
from src.services.order_service import OrderService

run_mappers()

work = WorkFlow()
work.register_service(InventoryService(service_name='Inventory Service',description='details of Inventory'))
work.register_service(OrderService(service_name='Order Service',description='details of Order'))
engine=Engine(work)

def lambda_handler(event, context):

    engine.execute(event)

    print(event)



    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
            "data":"success"
        }),
    }

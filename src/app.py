import json

from src.framework.etl_engine import Engine
from src.framework.workflow.work_flow_service import WorkFlowService
from src.mapper.orm_register import run_mappers
from src.services.Inventory_service import InventoryService
from src.services.order_service import OrderService


run_mappers()
work=WorkFlowService()
work.register_service(InventoryService())
work.register_service(OrderService())


def lambda_handler(event, context):

    engine=Engine(work)
    engine.execute(event)


    # order_service = OrderService(event)
    # order_service.validate_data()
    # order_service.process_data()
    # order_service.send_to_sqs()



    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
            "data":"success"
        }),
    }

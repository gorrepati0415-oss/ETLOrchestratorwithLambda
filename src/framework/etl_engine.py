import json
from src.framework.workflow.work_flow_main import WorkFlow


class Engine:
    def __init__(self,workflow: WorkFlow):
        self.event = None
        self.workflow=workflow

    def execute(self,event):
        event_name = json.loads(event['Records'][0]['body'])['header']['eventName']
        service = self.workflow.get_services(event_name)
        service.process_the_event(event)
        service.validate_data()
        service.send_to_sqs()
        service.process_data()

from src.framework.workflow.work_flow_service import WorkFlowService


class Engine:
    def __init__(self,workflow:WorkFlowService):
        self.workflow=workflow

    def execute(self,event):
        service = self.workflow.get_service("OrderPlaceEvent")
        service.process_the_event(event)
        service.validate_data()
        service.process_data()

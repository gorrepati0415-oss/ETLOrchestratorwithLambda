

class WorkFlow:

    def __init__(self):
        self.services=[]

    def register_service(self,service):
        self.services.append(service)

    def get_services(self,service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        raise Exception(f"{service_name} not found")








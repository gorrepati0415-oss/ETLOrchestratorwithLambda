from abc import ABC, abstractmethod


class EtlAbstractOrchestrator(ABC):

    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass


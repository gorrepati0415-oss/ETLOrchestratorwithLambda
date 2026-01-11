from src.model.inventry_model import InventryModel
from src.source.db_connection import SESSION_FACTORY


class InventryRepository:
    name="inventry"
    def __init__(self):
        self.session = SESSION_FACTORY()

    def insert(self, inventry_model: InventryModel):
        self.session.add(inventry_model)
        self.session.commit()
        return inventry_model

from typing import List, Optional
from pydantic import BaseModel, field_validator, ValidationError
from sqlalchemy import DECIMAL

from src.commons.Constants import allowed_status


class Items(BaseModel):
    sku: str
    qty: int

class OrderBody(BaseModel):
    order_id: str
    user_id: str
    items: Optional[List[Items]]=None
    total_amount: float
    payment_method: str
    status: str

    @field_validator('status')
    @classmethod
    def status_validator(cls, value):
        if value not in allowed_status:
            raise ValidationError('Invalid status value')
        return value


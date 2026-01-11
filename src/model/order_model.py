from dataclasses import dataclass
from datetime import datetime
from typing import Optional



@dataclass
class OrderModel:
    order_id: str
    user_id: str
    total_amount: float
    payment_method: str
    status: str
    created_at: Optional[datetime]  = None
    updated_at: Optional[datetime] = None

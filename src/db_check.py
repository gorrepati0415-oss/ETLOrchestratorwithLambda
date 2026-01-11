from src.model.order_model import OrderModel
from src.repositores.Order_repository import OrderRepository
from src.mapper.orm_register import run_mappers

order_dt=OrderModel(
    order_id='M2026',
    user_id='mohan1122',
    payment_method='MobilePay',
    status='complete',
    total_amount=1500.0)
run_mappers()
order_repo=OrderRepository()
order_repo.insert(order_dt)


from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

meta_data=MetaData()

inventry_tab = Table(
    'inventry_items',
    meta_data,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('order_id', String(50), nullable=False),
    Column('sku', String(100)),
    Column('status', String(20))
)

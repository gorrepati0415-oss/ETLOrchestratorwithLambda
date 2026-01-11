from sqlalchemy import MetaData, Table, Column, String, DECIMAL, text,DATETIME


metadata=MetaData()
order_table = Table("orders",metadata, Column("order_id",String(50), primary_key=True),
                    Column("user_id",String(50), nullable=False),
                    Column("total_amount",DECIMAL(10, 2), nullable=False),
                    Column("payment_method",String(30), nullable=False),
                    Column("status",String(20)),
                    Column("created_at",DATETIME,server_default=text("CURRENT_TIMESTAMP")),
                    Column("updated_at",DATETIME,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")))
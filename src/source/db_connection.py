from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.commons.Config import rds_protocol, rds_username, rds_password, rds_host, rds_port, rds_database_name


def get_connection():
    protocol=rds_protocol
    username=rds_username
    password=rds_password
    host=rds_host
    port=rds_port
    database=rds_database_name
    return f"{protocol}://{username}:{password}@{host}:{port}/{database}"

engine=create_engine(get_connection(),max_overflow=5,echo=False)

SESSION_FACTORY = sessionmaker(autocommit=False,autoflush=False,bind=engine)






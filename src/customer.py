import sqlalchemy as sa
from base import Base

class Customer(Base):
    __tablename__ = 'customer'
    customerid = sa.Column('customerid',sa.String(20), primary_key=True)
    customername = sa.Column('customername',sa.String(20))
    
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from customer import Customer

class dbmodel(object):
    db_config = ''
    engine = object

    def __init__(self, conn_string) -> None:
        self.engine = create_engine(conn_string)

    def get_customer_name_by_id(self, customer_id):
        Session = sessionmaker(bind=self.engine, future=True)
        session = Session()
        result = customer_id
        try:
            customer_row = session.execute(
                select(
                    Customer
                ).where(
                    Customer.customerid == customer_id
                )
            ).scalar_one_or_none()
            
            if customer_row is not None:
                result = customer_row.customername

            return result
        except Exception as ex:
            print(ex.args)
            return customer_id
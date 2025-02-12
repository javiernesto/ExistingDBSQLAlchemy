from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from customer import Customer
import pandas as pd


class dbmodel(object):
    db_config = ''
    engine = object

    def __init__(self, conn_string) -> None:
        self.engine = create_engine(conn_string)

    def get_customer_name_by_id(self, customer_id):
        Session = sessionmaker(bind=self.engine, future=True)
        session = session()
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

    def get_clients_by_country_state(
            self, 
            country, 
            state, 
            page=None, 
            rowsPerPage=None):
        df = pd.DataFrame()
        try:
            Session = sessionmaker(bind=self.engine, future=True)
            session = session()
            query_text = text(
                "execute dbo.SP_GetClientsByCountryState '{0}', '{1}'".format(country, state) 
                if page is None or rowsPerPage is None or page < 1 or rowsPerPage < 1 
                else
                "execute dbo.SP_GetClientsByCountryState '{0}', '{1}', {2}, {3}".format(country, state, page, rowsPerPage))
            query = session.execute(query_text)
            query_columns = query.keys() if query else []
            data = [dict(zip(query_columns, row)) for row in query.all()]

            # Saving the query data in a dataframe
            df = pd.DataFrame(data)
        except Exception as ex:
            print(ex.args)

        return df
    
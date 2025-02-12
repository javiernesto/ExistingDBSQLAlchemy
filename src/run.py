import sys
import dbmodel as db

def main(argv):
    user = 'YourUser'
    password = 'YourPassword'
    server = 'Server:Port'
    dbname = 'DataBase'
    connString = 'mssql+pyodbc://{0}:{1}@{2}/{3}?driver=SQL Server'.format(user, password, server, dbname)

    accountToGet = 'xxx'

    dbSQL = db.dbmodel(connString)

    ### Testing the function get_customer_name_by_id
    customer_name = dbSQL.get_customer_name_by_id(accountToGet)
    print(customer_name)

    ### Testing the function get_clients_by_country_state
    df_clients = dbSQL.get_clients_by_country_state('USA', 'TX', 1, 20)
    print(df_clients)


if __name__ == '__main__':
    main(sys.argv[1:])
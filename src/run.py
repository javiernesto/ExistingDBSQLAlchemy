import sys
import dbmodel as db

def main(argv):
    user = 'youruser'
    password = 'yourpassword'
    server = 'yourhost'
    dbname = 'yourdbname'
    connString = 'mssql+pyodbc://{0}:{1}@{2}/{3}?driver=SQL Server'.format(user, password, server, dbname)

    accountToGet = 'xxx'

    dbSQL = db.dbmodel(connString)
    customer_name = dbSQL.get_customer_name_by_id(accountToGet)
    print(customer_name)

if __name__ == '__main__':
    main(sys.argv[1:])
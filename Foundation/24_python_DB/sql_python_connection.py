import mysql.connector
from config import HOST, USER, PASSWORD


def connect_to_db(db_name):
    """
    Setup a connection to a database
    :param db_name: name of the database
    :return: db connection
    """
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_all_records():
    db_connection = None
    try:
        #  setup the db name that i want to connect
        db_name = 'tests'
        db_connection = connect_to_db(db_name)
        print('Connected to DB')

        # cursor that will execute the queries i run against my db
        cur = db_connection.cursor()
        query = f"""
        SELECT Item, Units, Total 
        FROM abcreport
        """
        cur.execute(query)
        result = cur.fetchall()

        for item in result:
            print(item)

        cur.close()

        # loop through result and print the output
    except Exception as e:
        print('Failed to connect to DB: %s' % e)
        # catch any errors that arise
    finally:
        #  if connection is Not None - i.e. it DID connect to a db within the try block, then we HAVE to close it down
        if db_connection is not None:
            # no matter what happend, pass/fail we always close the connection
            db_connection.close()



def calc_commission(result, commission):
    """
    calcualte the commission based on sales for a rep
    :param result: result set of the query
    :param commission: commision percent
    :return: commision value
    """

    sales = []

    for item in result:
        sales.append(item[2])

    commission = sum(sales) * (commission / 100)
    return commission




def get_all_records_for_rep(rep_name):
    db_connection = None
    comp = None
    try:
        #  setup the db name that i want to connect
        db_name = 'tests'
        db_connection = connect_to_db(db_name)
        print('Connected to DB')

        # cursor that will execute the queries i run against my db
        cur = db_connection.cursor()
        query = f"""
        SELECT Item, Units, Total 
        FROM abcreport
        WHERE Rep = '{rep_name}'
        """

        cur.execute(query)
        result = cur.fetchall()

        for item in result:
            print(item)

        comp = round(calc_commission(result, commission=10),2)
        print('Comp calculated: ', comp)

        cur.close()


    except Exception as e:
        print('Failed to connect to DB: %s' % e)
        # catch any errors that arise
    finally:
        #  if connection is Not None - i.e. it DID connect to a db within the try block, then we HAVE to close it down
        if db_connection is not None:
            # no matter what happend, pass/fail we always close the connection
            db_connection.close()

    return rep_name, comp






def insert_new_record(record):
    db_connection = None
    try:
        #  1 - connect to a db
        db_name = 'tests'
        db_connection = connect_to_db(db_name)
        print('Connected to DB')

    #     2 - create a cursor to query the db
        cur = db_connection.cursor()

        query = """
            INSERT INTO abcreport
            VALUES ( '{}', '{}', '{}', '{}', {}, {}, {}  ) 
        """.format(record['OrderDate'],
                   record['Region'],
                   record['Rep'],
                   record['Item'],
                   record['Units'],
                   record['UnitCost'],
                   record['Total'])
        print(query)
    #     3 - run the queries using the cursor
        cur.execute(query)
        db_connection.commit()

    #      close the cursor when finished querying
        cur.close()

    except:
        print('Error in connecting to DB')
    finally:
        if db_connection is not None:
            db_connection.close()



def main():
#     run the functions that access my DB
#     get_all_records()
#     get_all_records_for_rep('Morgan')
    record = {
        'OrderDate': "2020-12-15",
        'Region': "Central",
        "Rep": "Johnson",
        "Item": "post-it-notes",
        "Units": 220,
        "UnitCost": 2.5,
        "Total": 220 * 2.5
    }
    insert_new_record(record)
    second_record = {
            'OrderDate': "2020-12-15",
            'Region': "Central",
            "Rep": "Smith",
            "Item": "post-it-notes",
            "Units": 220,
            "UnitCost": 2.5,
            "Total": 220 * 2.5
        }
    insert_new_record(second_record)




if __name__ == '__main__':
    main()


#!/usr/bin/python

import psycopg2
from config import config


def creteTables():
    """ create tables in the PostgreSQL database"""
    
    commands = (
        """
        CREATE TABLE customers (
            cid SERIAL PRIMARY KEY,
            cname VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE products (
                pid SERIAL PRIMARY KEY,
                pname VARCHAR(255) NOT NULL,
                pprice numeric NOT NULL,
                prebate numeric
                )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertCustomer(cname):
    """ insert a new customer into the customers table """
    
    sql = """INSERT INTO customers(cname)
             VALUES(%s) RETURNING cid;"""
    conn = None
    cid = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (cname,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return cid

def insertCustomers(clist):
    """ insert multiple customers into the customers table  """
    
    sql = "INSERT INTO customers(cname) VALUES(%s)"
    
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, clist)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print(f'Inserted list of customers {clist}')


def insertProduct(pdict):
    """ insert multiple customers into the customers table  """

    from psycopg2.extensions import AsIs
    
    sql = 'insert into products(%s) values %s'
    
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        columns = pdict.keys()
        values = [pdict[col] for col in columns]
        cur.execute(sql, (AsIs(','.join(columns)), tuple(values)))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print(f'Inserted list of customers {pdict}')

def simulateProduct(rebate=0.1):
    ''' simulates product information '''

    import random
    pid = random.randint(1, 10)
    pname = str('P' + str(random.choice(range(10))))
    pprice = round(random.random()*100, 2)
    prebate = pprice*rebate

    return dict(pid=pid, pname=pname, pprice=pprice, prebate=prebate)

def insertProducts(n=5, rebate=0.1):

    ''' inserts multiple products '''

    import random

    for i in range(n):
        pid = i
        pname = str('p'+str(i))
        pprice = round(random.random()*100, 2)
        prebate = pprice*rebate
        pdict = dict(pid=pid, pname=pname, pprice=pprice, prebate=prebate)

        insertProduct(pdict)

def retrieveProductsData():

    ''' retrieves data using fetchall() method for given id '''
    
    sql = "select * from products"
    
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(sql)
        # FETCH details
        rows = cur.fetchall()
        products = []
        price = []
        rebate = []

        for r in rows:
            products.append(r[1])
            price.append(r[2])
            rebate.append(r[3])
        print(f'Products: {products} \n')
        print(f'Price: {price} \n')
        print(f'Rebate: {rebate} \n')
        print(f'The total amount of sales is: {sum(price)}, and the total rebate is: {sum(rebate)}') 

        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    

if __name__ == '__main__':
##    createTables()
##    insertCustomer('ms')
##    insertCustomers([('mk',), ('ms',), ('mya',), ('msb',)])
##    pdict = simulateProduct()
##    insertProduct(pdict)
##    insertProducts(n=5, rebate=0.1)
##    retrieveProductsData()

        

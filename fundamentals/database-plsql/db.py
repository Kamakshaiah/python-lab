from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.ini')

host = parser['postgresql']['host']
port = parser['postgresql']['port']

print(f'The connection to {parser.sections()} is opened at {host}:{port}') 

from psycopg2.extensions import AsIs
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database='postgres',
    user='postgres',
    password='postgres'
    )

product1 = {'pname': 'a', 'pprice': 123.12, 'prebate': 123.45}
columns = product1.keys()
columns
values = [product1[col] for col in columns]
sqlstmnt = 'insert into products(%s) values %s'
cur = conn.cursor()
cur.execute(sqlstmnt, (AsIs(','.join(columns)), tuple(values)))

cur.execute(sqlstmnt, (AsIs(','.join(columns)), tuple(values)))
cur.mogrify(sqlstmnt, (AsIs(','.join(columns)), tuple(values)))
conn.commit()

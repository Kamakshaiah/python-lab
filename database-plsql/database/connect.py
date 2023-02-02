import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None

    commands = (
        '''
            CREATE TABLE students (
                id serial,
                fname varchar,
                lname varchar
                )
        ''',
        '''
            \dt;
        '''

        )
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        
        for command in commands:
            cur.execute(command)
        
	# close the communication with the PostgreSQL
        cur.close()
        cur.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

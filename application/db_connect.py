import psycopg2
from db_config import config
import json
from db_tables import table
 
 
def connect(username):
    """ function for creating db connection object """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        # user=table(conn,username)
        return(conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
 
if __name__ == '__main__':
    connect()
import psycopg2
try:
    connection=psycopg2.connect(user="postgres",
                                password="Saiteja5b1@",
                                host="localhost",
                                port="5432",
                                database="example")
    cursor=connection.cursor()
    print("table before")
    command="""select * from saii"""
    cursor.execute(command)
    rows=cursor.fetchall()
    for row in rows:
        print(rows)
    # query="delete from saii where name=%s"
    # cursor.execute(query,(name, ))
    # connection.commit()
    # count=cursor.rowcount
    # print(count)
    # print("after updation")
    # command="select * from saii where name=%s;"
    # cursor.execute(command,(name, ))
    # record=cursor.fetchone()
    # print(record)
    
except(Exception,psycopg2.Error) as error:
    print("error is",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("connection is closed")
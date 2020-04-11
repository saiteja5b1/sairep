import psycopg2
import numpy as np
import operator
import pandas as pd
try:
    connection=psycopg2.connect(user="postgres",
                                password="Saiteja5b1@",
                                host="localhost",
                                port="5432",
                                database="project")
    cur=connection.cursor()
    query = "select crop_year from crop_data "
    years=cur.execute(query)
    record=cur.fetchall()
    nextt=np.unique(record)
    query1 = "select crop from crop_data "
    crops=cur.execute(query1)
    record1=cur.fetchall()
    nextt1=np.unique(record1)
    print(type(nextt1[0]))
    query1 = "select district_name from crop_data "
    cur.execute(query1)
    sam=cur.fetchall()
    dists=list(set(sam))
    d=sorted(dists,key=lambda x:x[0])
    ###  aa crop ki aa season lo ekkuva production vachindhi
    sample=pd.read_sql("select distinct(crop) from crop_data",connection)
    print(sample)

except(Exception,psycopg2.Error) as err:
    print(err)

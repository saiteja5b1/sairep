from pandas import DataFrame
import datetime
import json
import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
try:
    connection=psycopg2.connect(user="postgres",
                                password="Saiteja5b1@",
                                host="localhost",
                                port="5432",
                                database="project")
    cur=connection.cursor()
    # query="select * from predict01"
    # cur.execute(query)
    # results=cur.fetchone()
    # print(results)
    if cur!=None:
        try:
            quer="select distinct(crop) from crop_data where district_name='ANANTAPUR'"
            cur.execute(quer)
            val=cur.fetchall()
            # for cr in val:
            query=("select crop,crop_year,avg(production) from crop_data where crop='Rice' and district_name='KRISHNA' group by crop_year,crop order by crop_year,crop")
            cur.execute(query)
            val=cur.fetchall()
            res = [json.dumps(dict(record)) for record in val]
            print(res)
            # for i in val:
            #     print(i)
            connection.close()
            df=DataFrame(val,columns=['Crop','Crop_Year','Production'])
            print(df)
            # print(man)
            df.to_csv('file1.csv')
            data=pd.read_csv('file1.csv',header=None)
            mann=data.to_dict()
            # print(mann)
            # print(data.Crop_Year)
            # production=df.Production.astype(float)
            # year=df.Crop_Year.astype(int)
            # ye=df.Crop_Year.tolist()
            # print(type(ye[0]))
            # # print(df.Crop_Year)
            # # dates=[date for date in df.Crop_Year]
            # plt.xticks(year)
            # plt.yticks(prod)
            df.plot(x=data.Crop_Year,y=data.Production,kind='line')
            plt.show()
            # for va in val:
            #     print(va)
            #     p=pd.read_sql("select season,avg(production) from crop_data where crop='%s' and district_name='ANANTAPUR' group by season"%va,connection)
            #     s=p.max()
            #     if s.all()>last:
            #         s=last
            #         last=s
            # print(last)
        except(Exception,psycopg2.Error) as f:
            print(f)
                    # cur.execute(query)
                # vall=cur.fetchall()
                # for v in vall:
                #     print(v)
except(Exception,psycopg2.Error) as err:
    print(err)
    
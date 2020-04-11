import json,sys
from psycopg2 import connect,Error
from psycopg2.extras import Json
try:
        conn=connect(
            dbname="project",
            user="postgres",
            host="localhost",
            password="Saiteja5b1@",
            connect_timeout=3
        )
        cur=conn.cursor()
        print("\n created cursor")
except(Exception,Error) as err:
    print("\n psycopg2 connect")
    conn=None
    cur=None
table_name="crop_database"            
        # print(columns[0])
    # sql_string1+="(" + ','.join(columns) + ")\nVALUES "
    # values_str=""
    # for i, record in enumerate(columns):
    #     sql_string="INSERT INTO table_name(record) VALUES()"
    #     for v,val in enumerate(record):
    #         if type(val)==str:
    #             val=val.replace("'","'")
    #             val="'"+val+"'"
    #             # val_list=str(Json(val)).replace('"','')
    #             val_list+=[str(val)]
    #         values_str+="(" + ','.join(val_list) + "),\n"
    #         # print(values_str)
    #     sql_string="INSERT INTO %s (%s)\nVALUES %s" %(table_name,', '.join(map(column,val)),values_str)
if cur!=None:
        try:
            print("enterd")
            with open('datasets/dataset.json') as ds:
                record_list=json.load(ds)
                sql_string=""
                if type(record_list)==list:
                    # first_record=record_list[0]
                    columns=[list(x.keys()) for x in record_list]
                    values_list=[list(x.values()) for x in record_list]
                    for j,col in enumerate(columns):
                        for li in values_list:
                            some=list(li)
                            print(some)
                            i=0
                            for c in some:
                                if c == '':
                                    some[i]='0'
                                else:
                                    some[i]=str(c)
                                i+=1
                            some1=tuple(some)
                            cur.execute("INSERT INTO crop_data(State_Name,District_Name,Crop_Year,Season,Crop,Area,Production) VALUES(%r,%r,%r,%r,%r,%r,%r)"%some1)
                            conn.commit() 
                        break
                        # for val in values_list:
                        #     query="""INSERT INTO crop_data()
                        #     # if(type(val[i])==str):
                        #     #         sql_string="""INSERT INTO crop_data(%s) VALUES('%s')""" %(column,(val[i]) or (val[i]))
                        #     #         cur.execute(sql_string)
                        #     #         conn.commit()
                        #     # elif(type(val[i])==str):
                        #     #         sql_string="""INSERT INTO crop_data(%s) VALUES(int(%s))""" %(column,(int(val[i])))
                                    
                else:
                    print("needs an array")
                    sys.exit()

        except(Exception,Error) as error:
            print(error)
            conn.rollback()

conn.close()

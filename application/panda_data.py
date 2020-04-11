from db_connect import connect
import pandas.io.sql as psql
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

dbInstance=connect('yesu')
crop_data=psql.read_sql("select * from andhra_crop_details",dbInstance)
districts=crop_data['district_name'].unique()
crops=crop_data['crop'].unique()
years=crop_data['year'].unique()
# print(districts,crops,years,sep="\n")

""" yearwise production of different crops per acre """

yearly_average_crops=crop_data[['year','season','area','district_name','production','crop']].where((crop_data['district_name']=='PRAKASAM') & (crop_data['year']==date(2014,1,1))).groupby(["season",'year','district_name','crop']).mean()
yearly_crops=crop_data.loc[(crop_data['district_name']=='PRAKASAM') & (crop_data['year']==date(2014,1,1)),['crop','season']]
print(yearly_average_crops)

average_production=yearly_average_crops['production']/yearly_average_crops['area']
average=pd.Series(average_production,name='per(1acre)')
result=pd.concat([yearly_average_crops,average],axis=1)
# print(result)
# print(result[['crop','per(1acre)','district_name']].groupby('crop').mean())

""" total average production of the differnt crops per acre """

total_average=crop_data[['year','season','area','district_name','production','crop']].where((crop_data['district_name']=='KRISHNA')).groupby(['season','district_name','crop']).mean()
average_production=total_average['production']/total_average['area']
average=pd.Series(average_production,name='per(1acre)')
result=pd.concat([total_average,average],axis=1)
print(result)
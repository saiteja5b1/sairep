# from db_connect import connect
# def arabelle():
#     c=connect()
#     lis={}
#     g=['horticulture','food','cash','plantation']
#     total=[]
#     for i in g:
#         cg=[]
#         for  j in c:
#             if i==j[0]:
#                 cg.append(j[1])
#         total.append(cg)
#     print(total)


# arabelle()
import json
with open('datasets/arable.json') as f:
    c=json.load(f)
print(c.keys())
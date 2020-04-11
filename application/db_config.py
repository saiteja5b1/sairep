import json

def config():
    with open('D:/project/project$/application/database/user.json','r') as f:
        details=json.load(f)
    return(details)
    
       
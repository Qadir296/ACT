
import collections
from pygeohash import geohash
from lib import *


# create database 
cluster = MongoClient("mongodb+srv://user:act_test@cluster0.1qjcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["ACT"]
collection = db["location"]

d = {}
ControlServiceInfo= []
result = {}
def ControlserviceData(message):
        x = message['m2m:sgn']['nev']['rep']['m2m:cin']['con']
        location = x['location']
        y= x['DetectionNodeData']
        data = {"location": x}
        data1 = collection.insert_one(x)
        # if int(y['test_result']) <= 5:
        #   y=  {'forecast' : 'Green'}
         #  dict.update(y) 
        #else:
         #   z= {'forecast' : 'Green'}
          #  dict.update(z)
        #forecast_time = DateTimeRange("2021-03-22T10:00:00+0900", "2021-03-22T10:10:00+0900")
        msg = {'message' : 'Message from National Health Service'}
        #result.append(forecast_time)
        payload= {'m2m:cin': {'cnf': 'application/json:0', 'con': data}}
        new_payload= json.dumps(payload)
        write = requests.post(url= "https://icon-lab.tim.it/onem2m/act_test/ACT_ControlService", headers=headers, auth= HTTPBasicAuth('act_test', '@Test_99'), data=  new_payload)
        print(write.json())
        return write.status_code

def get_location_info(location_code):
    myquery = { "location" : location_code}
    mydoc = collection.find(myquery)
    # location_code  pgh.encode(a,b)
    for x in mydoc:
        print(x)
        d["location_data"]= x

    




        


## *Detection Node Server*:

from enum import Enum
import json
from typing import Optional
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from requests.auth import HTTPBasicAuth
from pip._vendor import requests
import time

app = FastAPI()

db = []

class DetectionData():
    def DetectionData():
        pheripheral_Id = input("enter the Pheripheral ID")
        status = ['active', 'sleeping', 'out-of-service', 'restarting', 'maintenance-requested', 'fault']
        test_time = datetime.now().isoformat()
        test_result = input("enter the result recorded")
        new_dict= {'status': status[0], 'Test_Time' : test_time, 'Test_Result': test_result}
        data= {pheripheral_Id : new_dict}
        return data
    def ICONData():
        new_dict1= {'m2m:cin': {'cnf': 'application/json:0', 'con': DetectionData.DetectionData()}}
        payload= json.dumps(new_dict1)
        headers= {'X-M2M-Origin': 'act_test_prod', 'X-M2M-RI': str(int(time.time())), 'content-Type': 'application/vnd.onem2m-res+json;ty=4',
        'Accept': 'application/json'}
        request= requests.post(url= "https://icon-lab.tim.it/onem2m/act_test/ACT_LocalService", headers=headers, auth= HTTPBasicAuth('act_test', '@Test_99'),
        data=  payload)
        r= request.json()
        return r
    ##def LocalServiceData():
        payload= DetectionData.DetectionData()
        headers= {'content-Type': 'application/json'}
        res= requests.post(url= "", headers= headers, data= payload)
        result= res.json()
        return result


icon_data = DetectionData.ICONData()
## local_serviceData = DetectionData.LocalServiceData()
print(icon_data)
class DetectionNodeData(BaseModel):
    command: str
    test_interval: int


@app.get("/")
def read_root():
    return {"Node": "ACT_Detection"}

@app.get("/node")
def read_item():
    result= []
    result.append(DetectionData.DetectionData())
    return result

  
@app.post("/node")
def add_data(data: DetectionNodeData):
    db.append(data.dict()) 
    return db[-1]
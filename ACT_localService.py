import socket
from pip._vendor import requests
import json
import time
from requests.auth import HTTPBasicAuth
import pygeohash as pgh
from datetime import datetime
from enum import Enum



def ACT_LocalTOControlService():
    # time_time
    test_time= datetime.now().isoformat()
    # test result value from user
    test_result= input("enter an integer value")


    data= {
    'geohash_code': pgh.encode(42.6, -5.6),'peripherial_id': '4A:54:4C:23:6D','test_result': 8,
    'test_time':'2021-06-30T14:41:09.415370','disinfection': False,'disinfection_time': '2021-06-30T15:41:40.423500'
    }
    new_dict= {'m2m:cin': {'cnf': 'application/json:0', 'con': data}}
    # converting dictionary to json
    payload = json.dumps(new_dict)

    # writing data to control service
    API_endpoint= "https://icon-lab.tim.it/onem2m/act_test/ACT_ControlService"

    print(payload)

    headers= {'X-M2M-Origin': 'act_test_prod', 'X-M2M-RI': str(int(time.time())), 'content-Type': 'application/vnd.onem2m-res+json;ty=4',
            'Accept': 'application/json'}
    response = requests.post(url= API_endpoint,  auth= HTTPBasicAuth('act_test', '@Test_99'),
                headers= headers,data= payload)
    print(response.json())

def ACT_LocalToDetectionService():
    comand_options= { 1: 'RESTART', 'SHUTDOWN' : 2, 'SLEEP' :3, 'STATUS_REQUEST' :4, 'TEST_START' : 5, 'TEST_STOP': 6}
    comand = comand_options.get(1)
    test_interval= 10
    data= {'command': comand, 'test_interval': test_interval}
    new_dict= {'m2m:cin': {'cnf': 'application/json:0', 'con': data}}
    # converting dictionary to json
    payload = json.dumps(new_dict)

    # writing data to control service
    API_endpoint= "https://icon-lab.tim.it/onem2m/act_test/ACT_DetectionNode7


    print(payload)

    headers= {'X-M2M-Origin': 'act_test_prod', 'X-M2M-RI': str(int(time.time())), 'content-Type': 'application/vnd.onem2m-res+json;ty=4',
            'Accept': 'application/json'}
    res = requests.post(url= API_endpoint,  auth= HTTPBasicAuth('act_test', '@Test_99'),
                headers= headers,data= payload)
    print (res.json())

print(" arranging data")
ACT_LocalToDetectionService()
ACT_LocalTOControlService()
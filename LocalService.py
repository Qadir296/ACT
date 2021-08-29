from os import get_exec_path
from tkinter.constants import COMMAND

from pip._vendor.urllib3.util.url import get_host
from lib import *
from ControlService import ControlserviceData, get_location_info, result, ControlServiceInfo

# TODO: need to send message to the Detection Node

LocalServiceData = {}

def LocalToControlService(message):
    #x = message['m2m:sgn']['sur']
    #if(x!= "/onem2m/act_test/ACT_DetectionNode/DetectionNodeNotify"):

    x = message['m2m:sgn']['nev']['rep']['m2m:cin']['con']  
    Disinfection= True;
    Disinfection_Time= datetime.now().isoformat()
    geohash_code = pgh.encode(30, -6.9)
    dict= {'location': geohash_code,'Disinfection': Disinfection, 'Disinfection_Time': Disinfection_Time, 'DetectionNodeData': x, 'Location-Service-Info': 'https://NationalHealth.com/forecast'}
    payload= {'m2m:cin': {'cnf': 'application/json:0', 'con': dict}}
    new_payload= json.dumps(payload)
    write = requests.post(url= "https://icon-lab.tim.it/onem2m/act_test/ACT_LocalService", headers=headers, auth= HTTPBasicAuth('act_test', '@Test_99'), data=  new_payload)
    print(write.json())
    return write.status_code

def LocalToDetectionNodeData(data):
    header= { 'content-Type':  'application/json'}
    get_host
    res = requests.post(url = "http://127.0.0.1:5000/DetectionService", headers = header , data = data)
    return res.status_code


    
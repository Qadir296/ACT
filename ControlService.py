from re import A
from lib import *

dict = {}
ControlServiceInfo= []
result = []
def ControlserviceData(message):
        x = message['m2m:sgn']['nev']['rep']['m2m:cin']['con']
        location = x['location']
        y= x['DetectionNodeData']
        data = {location: x}
        dict.update(data)
        if int(y['test_result']) <= 5:
           y=  {'forecast' : 'Green'}
           dict.update(y) 
        else:
            z= {'forecast' : 'Green'}
            dict.update(z)
        #forecast_time = DateTimeRange("2021-03-22T10:00:00+0900", "2021-03-22T10:10:00+0900")
        msg = {'message' : 'Message from National Health Service'}
        #result.append(forecast_time)
        dict.update(msg)
        payload= {'m2m:cin': {'cnf': 'application/json:0', 'con': data}}
        new_payload= json.dumps(payload)
        write = requests.post(url= "https://icon-lab.tim.it/onem2m/act_test/ACT_ControlService", headers=headers, auth= HTTPBasicAuth('username', 'password'), data=  new_payload)
        print(write.json())
        return write.status_code

def get_location_info(location_code):
    if location_code in dict.keys():
        values = dict[location_code]
        result.append(values)
    else:
        print("Record not found")
    




        


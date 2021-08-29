from lib import *

dataFromControlService= {}

longitude = input("enter the longitude  = ")
latitude = input("latitude = ")
time_frame = input("enter time FRAME = ")

header = {'content-Type' : 'application/json'}
res = requests.get(url = 'http://138.96.16.37:443/ControlService/location?', params= {'latitude': latitude, 'longitude': longitude}, headers = header )

print (res.status_code)

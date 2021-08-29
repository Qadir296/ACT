from flask import Flask, json,request, jsonify
from pip._vendor import requests
import json
import time
from requests.auth import HTTPBasicAuth
import pygeohash as pgh
from datetime import datetime

#test_time= datetime.now().isoformat()
#test_result= input("enter an integer value")

DetectionService = {}

api = Flask(__name__)


@api.route('/', methods=['POST', 'GET'])
def index():
  if(request.method== 'POST'):
    if request.content_type != 'application/vnd.onem2m-ntfy+json':
      data= request.get_json()
      return jsonify(data, "ERROR: Not FROM ICON" ), 201
    else:
      data = request.get_json()
      DetectionService.update(data)
      new_data= data.copy()
      payload= new_data["m2m:sgn"]["nev"]["rep"]["m2m:cin"]["con"]["value"]
      
      return jsonify(DetectionService, 201 ), 201
      
  else:
    return jsonify(DetectionService)


#@api.route('/DetectionService', methods=['POST'])
#def post_DetectionService(data):
 # DetectionService.update(data)
  #return json.dumps(DetectionService.update(data), 201)
 
if __name__ == '__main__':

    api.run(host= '138.96.16.37', port= 443 ,debug= True)
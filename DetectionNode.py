from lib import *

LocalServiceData= {}

def DetectionNodeData(message):
    payload= json.dumps(message)
    request= requests.post(url= "https://icon-lab.tim.it/onem2m/act_test/ACT_DetectionNode", headers=headers, auth= HTTPBasicAuth('username', 'password'),
      data=  payload)
    print(request.status_code)
    return request.json()

api = Flask(__name__)

@api.route('/DetectionService', methods=['POST', 'GET'])
def DetectionService():
  if(request.method== 'POST'):
    some_json = request.get_json()
    LocalServiceData.update(some_json)
    data= some_json.copy()
    DetectionNodeData(data)
    return jsonify(LocalServiceData), 201
  else:
    return jsonify(LocalServiceData)

if __name__ == '__main__':

    api.run(debug= True)



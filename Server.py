from lib import *
from ControlService import ControlserviceData, get_location_info, result, ControlServiceInfo
from LocalService import LocalServiceData, LocalToControlService


api = Flask(__name__)

@api.route('/LocalService', methods=['POST', 'GET'])
def LocalService():
    if(request.method== 'POST'):
        if request.content_type != 'application/vnd.onem2m-ntfy+json':
            data= request.get_json()
            return jsonify(data, "ERROR: Not FROM ICON" ), 201
        else:
            data = request.get_json()
            LocalServiceData.update(data)
            new_data= data.copy()
            LocalToControlService(new_data)
            return jsonify(LocalServiceData, 201 ), 201
    else:
        return jsonify(LocalServiceData)

@api.route('/ControlService', methods=['POST', 'GET'])
def ControlService():
    if(request.method== 'POST'):
        if request.content_type != 'application/vnd.onem2m-ntfy+json':
            data= request.get_data()
            return jsonify(result), 201
        else:
            data = request.get_json()
            ControlServiceInfo.append(data)
            new_data= data.copy()
            ControlserviceData(new_data)
            return jsonify(ControlServiceInfo, 201 ), 201
    else:
        return jsonify(result), 200
@api.route('/ControlService/location', methods=['GET'])
def location(): 
    a = request.args.get('latitude')
    b = request.args.get('longitude')
    location_code = pgh.encode(a,b)
    return jsonify(result), 200

if __name__ == '__main__':
    api.run(host= '10.188.35.12', port= 443 ,debug= True)
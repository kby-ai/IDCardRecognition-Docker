import sys
sys.path.append('.')

import os
import base64
import json

from flask import Flask, request, jsonify
from idsdk import getMachineCode
from idsdk import setActivation
from idsdk import initSDK
from idsdk import idcardRecognition

licensePath = "license.txt"
license = ""
# Reading machine code
machineCode = getMachineCode()
print("machineCode: ", machineCode.decode('utf-8'))

# Matching license from machine code
try:
    with open(licensePath, 'r') as file:
        license = file.read()
except IOError as exc:
    print("failed to open license.txt: ", exc.errno)
print("license: ", license)

# Activate SDK
ret = setActivation(license.encode('utf-8'))
print("activation: ", ret)

# Initialization SDK
ret = initSDK()
print("init: ", ret)

# Start Flask project
app = Flask(__name__) 

@app.route('/idcard_recognition', methods=['POST'])
def idcard_recognition():
    try:
        file = request.files['file']

        base64_image = base64.b64encode(file.read()).decode('utf-8')
        ret = idcardRecognition(base64_image.encode('utf-8'))

        if ret != None:
            j = json.loads(ret)
            j.update({"Status": "Ok"})
            response = jsonify(j)
        else:
            response = jsonify({"Status": "Error"})
    except:
        response = jsonify({"Status": "Error"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/idcard_recognition_base64', methods=['POST'])
def idcard_recognition_base64():
    try:
        content = request.get_json()
        base64_image = content['base64']

        ret = idcardRecognition(base64_image.encode('utf-8'))

        if ret != None:
            j = json.loads(ret)
            j.update({"Status": "Ok"})
            response = jsonify(j)
        else:
            response = jsonify({"Status": "Error"})
    except:
        response = jsonify({"Status": "Error"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
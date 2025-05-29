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

# Get a specific environment variable by name
license = os.environ.get("LICENSE")

# Check if the variable exists
if license is not None:
    print("Value of LICENSE:", license)
else:
    license = ""
    try:
        with open(licensePath, 'r') as file:
            license = file.read().strip()
    except IOError as exc:
        print("failed to open license.txt: ", exc.errno)
    print("license: ", license)

machineCode = getMachineCode()
print("machineCode: ", machineCode.decode('utf-8'))

ret = setActivation(license.encode('utf-8'))
print("activation: ", ret)

ret = initSDK()
print("init: ", ret)

app = Flask(__name__) 

@app.route('/idcard_recognition', methods=['POST'])
def idcard_recognition():
    try:
        file = request.files['file']

        base64_image = base64.b64encode(file.read()).decode('utf-8')
        ret = idcardRecognition(base64_image.encode('utf-8'), "".encode('utf-8'))

        if ret != None:
            j = json.loads(ret)
            j.update({"Status": "Ok"})
            response = jsonify(j)
        else:
            response = jsonify({"Status": "Processing Failed"})
    except:
        response = jsonify({"Status": "Image Error"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/idcard_recognition_multi_page', methods=['POST'])
def idcard_recognition_multi_page():
    base64_image1 = ""
    base64_image2 = ""
    try:
        file1 = request.files['file1']
        base64_image1 = base64.b64encode(file1.read()).decode('utf-8')
    except:
        response = jsonify({"Status": "Front Image Error"})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    try:
        file2 = request.files['file2']
        base64_image2 = base64.b64encode(file2.read()).decode('utf-8')
    except:
        base64_image2 = ""
        
    ret = idcardRecognition(base64_image1.encode('utf-8'), base64_image2.encode('utf-8'))

    if ret != None:
        j = json.loads(ret)
        j.update({"Status": "Ok"})
        response = jsonify(j)
    else:
        response = jsonify({"Status": "Processing Failed"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/idcard_recognition_base64', methods=['POST'])
def idcard_recognition_base64():
    try:
        content = request.get_json()
        base64_image = content['base64']

        ret = idcardRecognition(base64_image.encode('utf-8'), "".encode('utf-8'))

        if ret != None:
            j = json.loads(ret)
            j.update({"Status": "Ok"})
            response = jsonify(j)
        else:
            response = jsonify({"Status": "Processing Failed"})
    except:
        response = jsonify({"Status": "Image Error"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/idcard_recognition_base64_multi_page', methods=['POST'])
def idcard_recognition_base64_multi_page():
    base64_image1 = ""
    base64_image2 = ""

    try:
        content = request.get_json()
        base64_image1 = content['base64_1']
    except:
        response = jsonify({"Status": "Front Image Error"})

        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    try:
        content = request.get_json()
        base64_image2 = content['base64_2']
    except:
        base64_image2 = ""

    ret = idcardRecognition(base64_image1.encode('utf-8'), base64_image2.encode('utf-8'))

    if ret != None:
        j = json.loads(ret)
        j.update({"Status": "Ok"})
        response = jsonify(j)
    else:
        response = jsonify({"Status": "Processing Failed"})

    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

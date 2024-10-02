<p align="center">
  <a href="https://play.google.com/store/apps/dev?id=7086930298279250852" target="_blank">
    <img alt="" src="https://github-production-user-asset-6210df.s3.amazonaws.com/125717930/246971879-8ce757c3-90dc-438d-807f-3f3d29ddc064.png" width=500/>
  </a>  
</p>

#### 📚 Product & Resources - [Here](https://github.com/kby-ai/Product)
#### 🛟 Help Center - [Here](https://docs.kby-ai.com)
#### 💼 KYC Verification Demo - [Here](https://github.com/kby-ai/KYC-Verification-Demo-Android)
#### 🙋‍♀️ Docker Hub - [Here](https://hub.docker.com/r/kbyai/idcard-recognition)
```bash
sudo docker pull kbyai/idcard-recognition:latest
sudo docker run -e LICENSE="xxxxx" -p 8082:8080 -p 9002:9000 kbyai/idcard-recognition:latest
```

# IDCardRecognition-Docker

## Introduction

This repo demonstrates the server-based recognition capabilities for `ID card`, `passport`, and `driver's license`.<br/>
At the core of this project lies the `ID Card Recognition SDK`, which has been developed to provide comprehensive support for recognizing `ID card`, `passport`, and `driver's license` from 200+ countries.

### ◾ID Card Recognition SDK Main Functionalities

  | Surpported ID Type      | Functionalities | Release Type |
  |------------------|------------------|------------------|
  | ID Card        | Extracting Information(OCR)    | Android(`Kotlin & Java`) |
  | Passport        | Scanning Barcode    | iOS(`Swift & Objectiv-C`) |
  | Driver License        | Parsing MRZ    | Flutter(`Dart`) |
  |         | Auto Capturing    | Web Front-end(`Javascript`) |
  |         | Scanning QR code        | Server-Windows(`Python`) |
  |         | Supporting 200+ Countries' ID Documents        | Server-Linux(`Python`) |
  |         | Supporting 130+ Languages        |  |
  |         | ID Document Detection        |  |

### ◾ID Card Recognition Product List
  | No.      | Repository | Release Type |
  |------------------|------------------|------------------|
  | 1        | [ID Card Recognition - Android](https://github.com/kby-ai/IDCardRecognition-Android)    | Android |
  | 2        | [ID Card Recognition - iOS](https://github.com/kby-ai/IDCardRecognition-iOS)    | iOS |
  | 3        | [ID Card Recognition - Flutter](https://github.com/kby-ai/IDCardRecognition-Flutter)    | Flutter |
  | 4        | [ID Auto Capture - React](https://github.com/kby-ai/ID-document-capture-React)    | Web Front-end |
  | 5        | [ID Card Recognition - Windows](https://github.com/kby-ai/IDCardRecognition-Windows)        | Server-Windows |
  | ➡️        | <b>[ID Card Recognition - Linux](https://github.com/kby-ai/IDCardRecognition-Docker)</b>        | <b>Server-Linux</b> |

## Try the API
### Online Demo
  You can test the SDK using images [here](https://web.kby-ai.com).</br>  
  ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/ff395174-d3e9-4198-bfc8-6024a8c31734)

### Documentation
https://docs.kby-ai.com/help/product/id-card-sdk

### Postman
  To test the `API`, you can use `Postman`. Here are the endpoints for testing:
  - Test with an image file: Send a `POST` request to `http://18.221.33.238:8082/idcard_recognition`.
  - Test with a `base64-encoded` image: Send a `POST` request to `http://18.221.33.238:8082/idcard_recognition_base64`.

    You can download the `Postman` collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/IDCardRecognition-Docker/tree/main/postman/kby-ai-idcard.postman_collection.json)
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/0ec93826-76d7-47a7-9065-6bd353bc79b3)

## SDK License

This project uses `KBY-AI`'s `ID card recognition server SDK`, which requires a license per machine.

- The code below shows how to use the license: https://github.com/kby-ai/IDCardRecognition-Docker/blob/9f8138fa83d39a80a95e71b52048dbfc6579558c/app.py#L14-L25

- To request the license, please provide us with the `machine code` obtained from the `getMachineCode` function.

#### Please contact us:</br>
🧙`Email:` contact@kby-ai.com</br>
🧙`Telegram:` [@kbyai](https://t.me/kbyai)</br>
🧙`WhatsApp:` [+19092802609](https://wa.me/+19092802609)</br>
🧙`Skype:` [live:.cid.66e2522354b1049b](https://join.skype.com/invite/OffY2r1NUFev)</br>
🧙`Facebook:` https://www.facebook.com/KBYAI</br>

## How to run

### 1. System Requirements
  - CPU: 2 cores or more (Recommended: 2 cores)
  - RAM: 4 GB or more (Recommended: 8 GB)
  - HDD: 4 GB or more (Recommended: 8 GB)
  - OS: Ubuntu 20.04 or later

### 2. Setup and Test
  - Clone the project:
    ```bash
    git clone https://github.com/kby-ai/IDCardRecognition-Docker.git
    ```
  - Download the model from `Google Drive`: [click here](https://drive.google.com/file/d/1fmTUG7a9IoMA8QiXR9A0xf3Cr6D5UkdC/view)
    ```bash
    cd IDCardRecognition-Docker
    
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1fmTUG7a9IoMA8QiXR9A0xf3Cr6D5UkdC' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1fmTUG7a9IoMA8QiXR9A0xf3Cr6D5UkdC" -O data.zip && rm -rf /tmp/cookies.txt
    
    unzip data.zip
    ```
  - Build the `Docker` image:
    ```bash
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-idcard:latest .
    ```
  - Run the `Docker` container:
    ```bash
    sudo docker run -v ./license.txt:/root/kby-ai-idcard/license.txt -p 8082:8080 kby-ai-idcard
    ```
  - Send us the `machine code` and then we will give you a `license key`.
  
    After that, update the `license.txt` file by overwriting the license key that you received. Then, run the `Docker` container again.
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/deab4a80-ae99-4646-a37d-b1441cff4dde)
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/7994cecd-05fb-42e7-a21d-986da0e2d796)

  - To test the `API`, you can use `Postman`. Here are the endpoints for testing:

    Test with an image file: Send a `POST` request to `http://{xx.xx.xx.xx}:8082/idcard_recognition`.
    
    Test with a `base64-encoded` image: Send a `POST` request to `http://{xx.xx.xx.xx}:8082/idcard_recognition_base64`.
    
    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/IDCardRecognition-Docker/tree/main/postman/kby-ai-idcard.postman_collection.json)

### 3. Execute the Gradio demo
  - Setup Gradio
    Ensure that you have the necessary dependencies installed. 
    
    `Gradio` requires `Python 3.6` or above. 
    
    You can install Gradio using pip by running the following command:
    ```bash
    pip install gradio
    ```
  - Run the demo
    Run it using the following command:
    ```bash
    cd gradio
    python demo.py
    ```
  - You can test within the following `URL`:    
    `http://127.0.0.1:9000`
    
## About SDK

### 1. Initializing the SDK

- Step One

  First, obtain the `machine code` for activation and request a license based on the `machine code`.
  ```python
  machineCode = getMachineCode()
  print("machineCode: ", machineCode.decode('utf-8'))
  ```
  
- Step Two

  Next, activate the `SDK` using the received license.
  ```python
  setActivation(license.encode('utf-8'))
  ```  
  If activation is successful, the return value will be `SDK_SUCCESS`. Otherwise, an error value will be returned.

- Step Three

  After activation, call the initialization function of the `SDK`.
  ```python
  initSDK()
  ```
  If initialization is successful, the return value will be `SDK_SUCCESS`. Otherwise, an error value will be returned.

### 2. APIs

  - ID Card Recognition

    The SDK provides a single `API` for `ID card recognition`.
    
    The function can be used as follows:

    ```python
    ret = idcardRecognition(base64_image.encode('utf-8'))
    ```
    
    The function accepts only one parameter, which should be the `base64-encoded` format of the image (e.g., `JPG`, `PNG`, etc.).

    If the recognition is successful, the function will return a `JSON-formatted` string containing the recognized information. In case of failure, the return value will be `NULL`.

[![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fgithub.com%2Fkby-ai%2FIDCardRecognition-Docker&countColor=%23263759)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fkby-ai%2FIDCardRecognition-Docker)

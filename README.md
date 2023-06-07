<p align="left">
  <img src="https://user-images.githubusercontent.com/125717930/225975240-24b9a8ad-8cc6-4d5f-9a91-1435951b0bd7.png" width="120" alt="Nest Logo" />
</p>

👏  We have published the Face Liveness Detection, Face Recognition SDK and ID Card Recognition SDK for the server.

  - [FaceLivenessDetection-Docker](https://github.com/kby-ai/FaceLivenessDetection-Docker)

  - [FaceRecognition-Docker](https://github.com/kby-ai/FaceRecognition-Docker)

  - [IDCardRecognition-Docker](https://github.com/kby-ai/IDCardRecognition-Docker)

# IDCardRecognition-Docker

## Introduction

The demo project demonstrates the server-based recognition capabilities for ID cards, passports, and driver's licenses.

At the core of this project lies the ID Card Recognition SDK, which has been developed to provide comprehensive support for recognizing ID cards, passports, and driver's licenses from over 180 countries.

> The demo is integrated with KBY-AI's ID Card Recognition Server SDK.

> For other solutions, please explore the following:
> - [Face Liveness Detection - Android(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-Android)
> - [Face Liveness Detection - iOS(Basic SDK)](https://github.com/kby-ai/FaceLivenessDetection-iOS)
> - [Face Recognition - Android(Stdndard SDK)](https://github.com/kby-ai/FaceRecognition-Android)
> - [Face Recognition - iOS(Standard SDK)](https://github.com/kby-ai/FaceRecognition-iOS)
> - [Face Recognition - Flutter(Standard SDK)](https://github.com/kby-ai/FaceRecognition-Flutter)
> - [Face Attribute - Android(Premium SDK)](https://github.com/kby-ai/FaceAttribute-Android)
> - [Face Attribute - iOS(Premium SDK)](https://github.com/kby-ai/FaceAttribute-iOS)

## Try the API
### Online Demo
  You can test the SDK using images from the following URL:
  https://web.kby-ai.com/
  
  ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/ff395174-d3e9-4198-bfc8-6024a8c31734)
  
### Postman
  To test the API, you can use Postman. Here are the endpoints for testing:
  - Test with an image file: Send a POST request to http://18.221.33.238:8082/idcard_recognition
  - Test with a base64-encoded image: Send a POST request to http://18.221.33.238:8082/idcard_recognition_base64

    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/IDCardRecognition-Docker/tree/main/postman/kby-ai-idcard.postman_collection.json)
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/0ec93826-76d7-47a7-9065-6bd353bc79b3)

## SDK License

This project uses KBY-AI's Face Recognition Server SDK, which requires a license per machine.

- The code below shows how to use the license: https://github.com/kby-ai/IDCardRecognition-Docker/blob/9f8138fa83d39a80a95e71b52048dbfc6579558c/app.py#L14-L25

- In order to request the license, please provide us with the machine code obtained from the "getMachineCode" function.

  Please contact us:
  ```
  Email: contact@kby-ai.com

  Telegram: @kbyai

  WhatsApp: +19092802609

  Skype: live:.cid.66e2522354b1049b

## How to run

### 1. System Requirements
  - CPU: 2 cores or more (Recommended: 2 cores)
  - RAM: 4 GB or more (Recommended: 8 GB)
  - HDD: 4 GB or more (Recommended: 8 GB)
  - OS: Ubuntu 20.04 or later

### 2. Setup and Test
  - Clone the project:
    ```
    git clone https://github.com/kby-ai/IDCardRecognition-Docker.git
    ```
  - Download the model from Google Drive: [click here](https://drive.google.com/file/d/19vA7ZOlo19BcW8v4iCoCGahUEbgKCo48/view?usp=sharing)
    ```
    cd IDCardRecognition-Docker
    
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1fmTUG7a9IoMA8QiXR9A0xf3Cr6D5UkdC' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1fmTUG7a9IoMA8QiXR9A0xf3Cr6D5UkdC" -O data.zip && rm -rf /tmp/cookies.txt
    
    unzip data.zip
    ```
  - Build the Docker image:
    ```
    sudo docker build --pull --rm -f Dockerfile -t kby-ai-idcard:latest .
    ```
  - Run the Docker container:
    ```
    sudo docker run -v ./license.txt:/root/kby-ai-idcard/license.txt -p 8082:8080 kby-ai-idcard
    ```
  - Send us the machine code and replace the license.txt file you received. Then, run the Docker container again.
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/deab4a80-ae99-4646-a37d-b1441cff4dde)
    
    ![image](https://github.com/kby-ai/IDCardRecognition-Docker/assets/125717930/7994cecd-05fb-42e7-a21d-986da0e2d796)

  - To test the API, you can use Postman. Here are the endpoints for testing:

    Test with an image file: Send a POST request to http://{xx.xx.xx.xx}:8082/idcard_recognition
    
    Test with a base64-encoded image: Send a POST request to http://{xx.xx.xx.xx}:8081/idcard_recognition_base64
    
    You can download the Postman collection to easily access and use these endpoints. [click here](https://github.com/kby-ai/IDCardRecognition-Docker/tree/main/postman/kby-ai-idcard.postman_collection.json)

### 3. Execute the Gradio demo
  - Setup Gradio
    Ensure that you have the necessary dependencies installed. 
    
    Gradio requires Python 3.6 or above. 
    
    You can install Gradio using pip by running the following command:
    ```
    pip install gradio
    ```
  - Run the demo
    Run it using the following command:
    ```
    cd gradio
    python demo.py
    ```
  - You can test within the following URL:    
    http://127.0.0.1:9000
    
## About SDK

### 1. Initializing the SDK

- Step One

  First, obtain the machine code for activation and request a license based on the machine code.
  ```
  machineCode = getMachineCode()
  print("machineCode: ", machineCode.decode('utf-8'))
  ```
  
- Step Two

  Next, activate the SDK using the received license.
  ```
  setActivation(license.encode('utf-8'))
  ```  
  If activation is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

- Step Three

  After activation, call the initialization function of the SDK.
  ```
  initSDK()
  ```
  If initialization is successful, the return value will be SDK_SUCCESS. Otherwise, an error value will be returned.

### 2. APIs

  - ID Card Recognition

    The SDK provides a single API for ID card recognition.
    
    The function can be used as follows:

    ```
    ret = idcardRecognition(base64_image.encode('utf-8'))
    ```
    
    The function accepts only one parameter, which should be the base64-encoded format of the image (e.g., JPG, PNG, etc.).

    If the recognition is successful, the function will return a JSON-formatted string containing the recognized information. In case of failure, the return value will be NULL.

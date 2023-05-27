#pragma once

#ifdef __cplusplus
extern "C" {
#endif

enum SDK_ERROR
{
	SDK_SUCCESS = 0,
	SDK_LICENSE_KEY_ERROR = -1,
	SDK_LICENSE_APPID_ERROR = -2,
	SDK_LICENSE_EXPIRED = -3,
	SDK_NO_ACTIVATED = -4,
	SDK_INIT_ERROR = -5,
};


/*
* Get the machine code for SDK activation
*/
const char* getMachineCode();

/*
* Activate the SDK using the provided license
*/

int setActivation(char* license);

/*
* Initialize the SDK with the specified model path
*/
int initSDK();

/*
* The function accepts only one parameter, which should be the base64-encoded format of the image (e.g., JPG, PNG, etc.).
* If the recognition is successful, the function will return a JSON-formatted string containing the recognized information. In case of failure, the return value will be NULL.
*/
char* idcardRecognition(char* image_base64);

#ifdef __cplusplus
}
#endif

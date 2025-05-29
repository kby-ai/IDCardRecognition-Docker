import os

from ctypes import *

libPath = os.path.abspath(os.path.dirname(__file__)) + '/libkbyai_idsdk.so'
idsdk = cdll.LoadLibrary(libPath)

getMachineCode = idsdk.getMachineCode
getMachineCode.argtypes = []
getMachineCode.restype = c_char_p

setActivation = idsdk.setActivation
setActivation.argtypes = [c_char_p]
setActivation.restype = c_int32

initSDK = idsdk.initSDK
initSDK.argtypes = []
initSDK.restype = c_int32

idcardRecognition = idsdk.idcardRecognition
idcardRecognition.argtypes = [c_char_p, c_char_p]
idcardRecognition.restype = c_char_p


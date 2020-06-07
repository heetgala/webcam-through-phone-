import urllib.request
import cv2
import numpy as np

while True:
    imgResp=urllib.request.urlopen('http://192.168.0.103:8080/shot.jpg')
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)

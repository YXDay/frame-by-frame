#coding:utf-8

import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/daiyanxu/Desktop/project/me/HumanActionRecognition/classification_core/static/images/video_train/run/video_distinguish.m4v')

fgbg = cv2.BackgroundSubtractorMOG(50, 20, 0)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

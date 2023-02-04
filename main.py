import cvzone
import cv2
import numpy
import pandas
print("HI")
cap = cv2.VideoCapture(0)
while True:

    _, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)

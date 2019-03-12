import argparse
import cv2
import numpy
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the File")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray,75,200)
cv2.imshow("Original",image)
cv2.imshow("Edged",edged)
(img,cnts,his)=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:7]
for c in cnts:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.01*peri,True)
    print("Original:{}, Approx:{}".format(len(c),len(approx)))
    if len(approx) == 4 :
        cv2.drawContours(image,[approx],-1,(0,255,0),2)
cv2.imshow("Output",image)
cv2.waitKey(0)
import numpy as np
import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

(a,cnts,b)=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for (i,c) in enumerate(cnts):
    #computing the area of the countor along with the bounding box for computing aspect ratio
    area=cv2.contourArea(c)
    (x,y,w,h)=cv2.boundingRect(c)
    #compute the convex hull of the contour and then calculate the area of the convex hull to compute the solidiy
    hull=cv2.convexHull(c)
    hullarea=cv2.contourArea(hull)
    solidity=area/float(hullarea)
    #initialize the character Text
    char="?"
    #if solidity is high then it is O
    if solidity > 0.9:
        char="O"
    #else if the solidty s still resonably high we will find for x
    elif solidity >= .5:
        char="X"

    #if character is not uunknown draw if
    if char!="?":
        cv2.drawContours(image, [c], -1, (0,255,0), 3)
        cv2.putText(image,"#{}{}".format(char,i+1), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0,255,0), 4)
        print("#{}--Contour{}--Solidity={}".format(char, i+1, solidity))
      #  print("#{}".format(char))
       # print("Contour{}".format(i+1))
        #print("Solidity{}".format(solidity))

cv2.imshow("Output", image)
cv2.waitKey(0)
import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the file")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#thresh=cv2.threshold(gray,255,255,cv2.THRESH_BINARY_INV)[1]
thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Origianl",image)
cv2.imshow("Gray",gray)
cv2.imshow("Threshold",thresh)
cv2.waitKey(0)
# Find External Contours in the threshold image and allocate the memory for the convex hull image
(a,cnts,hist)=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
hullimage=np.zeros(gray.shape[:2],dtype="uint8")
cv2.imshow("Convex Hull",hullimage)
cv2.waitKey(0)
for (i,c) in enumerate(cnts):
    #find teh area of the countor along with the bounding box to find the ratio
    area=cv2.contourArea(c)
    (x,y,w,h)=cv2.boundingRect(c)
    #compute the aspect ratio of the contour which is simply the widht divided by the hight of bounding box
    aspectRatio=w/float(h)
    # use the areao of the contour and the w, h to find the area of the bounding box o compute the extent
    extent=area/float(w*h)
    #compute the convex hull of the contour and then calucate the solidiy =area/area encllosed by convex hull
    hull=cv2.convexHull(c)
    hullArea=cv2.contourArea(hull)
    solidity=area/float(hullArea)
    #visualise the original contours anbd the convex hull and inistialise the name of the shape
    cv2.drawContours(hullimage,[hull],-1,255,-1)
    cv2.drawContours(image,[c],-1,(240,0,159),3)
    shape=""


    #if aspect Ratio is near 1 then it is likely to be a squuare
    if aspectRatio >=- .98 and aspectRatio <=1.02:
        shape="SQUARE"
    #if width is 3 times longer then length then shape is rectangle
    elif aspectRatio >= 3.0:
        shape="rectangle"
    # if the extent is sufficiently small then we have a L piece
    elif extent <= 0.26:
        shape="L-Piece"
    #if the solididty is large enough we have a Z piece
    elif solidity > 0.80:
        shape="Z-Piece"

    #Draw the Shape name on the image
    cv2.putText(image,"#{}-{}".format(i+1,shape),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(240,0,159),2)
    print("Contour #{}--aspect Ratia= {}--,extent= {},solidity={}".format(i+1,aspectRatio,extent,solidity))
    cv2.imshow("Convex Hull",hullimage)
    cv2.imshow("New Image",image)
    cv2.waitKey(0)
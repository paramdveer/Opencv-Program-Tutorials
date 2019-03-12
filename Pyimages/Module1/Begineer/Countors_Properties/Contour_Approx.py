import argparse
import cv2
import numpy
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the File")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#find contours in the image
(im,cnts,hist)=cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for (i,c) in enumerate(cnts):
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.01*peri,True)
    #if the approximated contour has 4 vertices we are examining a rectangle
    if len(approx) == 4:
        #draw the outline of the contour and draw the text on the image
        cv2.drawContours(image,[c],-1,(0,255,255),2)
        (x,y,w,h)=cv2.boundingRect(approx)
        cv2.putText(image,"Rectangle No{}".format(i+1),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)

#show the out put image
cv2.imshow("Output",image)
cv2.waitKey(0)


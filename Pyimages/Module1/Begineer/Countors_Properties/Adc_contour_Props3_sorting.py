import argparse
import cv2
import numpy as np
import sort_contours

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image in which we want to sort the countours")
ap.add_argument("-m","--method",required=True,help="Sorting Method")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
accumEdged=np.zeros(image.shape[:2],dtype="uint8")

# looping over the Red green and bklue channels respectively
i=0
for chan in cv2.split(image):
    #blurr the channel, extract edges from it and accumlate the set of edges of teh image
    chan=cv2.medianBlur(chan,11)
    edged=cv2.Canny(chan,50,200)
    cv2.waitKey(0)
    cv2.imshow("Channel#{}".format(i+1),edged)
    accumEdged = cv2.bitwise_or(accumEdged, edged)
    i+=1

#show the accumed Edge Maped
cv2.waitKey(0)
cv2.imshow("Edge Map",accumEdged)
cv2.waitKey(0)
# find the contours in the accumEdged image and keep only the bigger ones
(img,cnts,hist)=cv2.findContours(accumEdged.copy(),cv2.RETR _EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
orig=image.copy()

for (i,c) in enumerate(cnts):
    orig=sort_contours.draw_contours(orig,c,i)

#show the unsorted contours and draw them
cv2.waitKey(0)
cv2.imshow("unsorted",orig)

(cnts,boundingBoxes)=sort_contours.sort_countours(cnts,method=args["method"])

for (i,c) in enumerate (cnts):
    image=sort_contours.draw_contours(image,c,i)

#show the output image
cv2.imshow("Sorted",image)
cv2.waitKey(0)
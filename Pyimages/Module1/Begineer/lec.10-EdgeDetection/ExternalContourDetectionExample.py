import cv2
import argparse
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)
(a,cnts,c)=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("The number of countours are {}".format(len(cnts)))
clone=image.copy()
cv2.drawContours(clone,cnts,-1,(0,0,255),2)
cv2.imshow("Countors ",clone)
cv2.waitKey(0)
cv2.destroyAllWindows()
clone=image.copy()
"""
for (i,c) in enumerate(cnts):
    print("Drawing the Counter #{}".format(i+1))
    cv2.drawContours(clone,[c],-1,(0,255,0),2)
    cv2.imshow("Single Countour",clone)
    cv2.waitKey(0)
   """
cv2.destroyAllWindows()
clone=image.copy()
i=0
for c in cnts:
    print("Drawing the Counter #{}".format(i+1))
    cv2.drawContours(clone,cnts,i,(0,255,0),2)
    i=i+1
    cv2.imshow("Single Countour",clone)
    mask1=np.zeros(image.shape,dtype="uint8")
    cv2.drawContours(mask1,[c],-1,255,-1)
    cv2.imshow("Mask",mask1)
    cv2.waitKey(0)
    cv2.imshow("Mask Applied",cv2.bitwise_and(image,image,mask=mask1))
    cv2.waitKey(0)


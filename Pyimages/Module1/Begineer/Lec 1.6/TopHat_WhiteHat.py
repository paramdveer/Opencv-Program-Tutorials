import argparse
import cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the File")
args=vars(ap.parse_args())

#Load The image andd convert it to grayScale
image=cv2.imread(args["image"])
cv2.imshow("Original",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#To perform Top hat / White Hat operation
#Enabkles us to find light Regions in dark background
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
whiteHatOp=cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,kernel)

# To perform Black hat operation
#Enables us to find the dark Regions in Bright Background
BlackHatOp=cv2.morphologyEx(gray,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("TopHat/WhiteHat",whiteHatOp)
cv2.imshow("BlackHat",BlackHatOp)
cv2.waitKey(0)
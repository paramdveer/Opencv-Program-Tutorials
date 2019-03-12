import argparse
import numpy
import imutils
import cv2
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args= vars(ap.parse_args())
image=cv2.imread(args["image"])
cv2.imshow("Original",image)

#flipping horizontlly around y axis
image2=cv2.flip(image,1)
cv2.imshow("Horizontal Flip",image2)

#Flipping vertically
cv2.flip(image,0,image2)
cv2.imshow("Flipped Vertically",image2)

#flipping horizontally and vertically
cv2.flip(image,-1,image2)
cv2.imshow("Flipped Vertically and horizontally",image2)
cv2.waitKey(0)
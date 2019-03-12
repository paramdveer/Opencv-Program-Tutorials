import argparse
import numpy
import imutils
import cv2
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args= vars(ap.parse_args())
image=cv2.imread(args["image"])
cv2.imshow("Original",image)


#image2=image[85:240,85:255]
#cv2.imshow("Cropped1",image2)
#image2=image[85:200,100:280]
#cv2.imshow("Cropped2",image2)
cv2.waitKey(0)
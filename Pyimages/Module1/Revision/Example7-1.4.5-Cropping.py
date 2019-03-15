"""
Croping: Selecting a region of Interest(ROI) from the image out of the image
To Crop Simply we can use the Slicing of the array
-------------------------------------------------------
image[Start-Y:End-Y, start-X:End-X]
--------------------------------------------------------
by just using the array slicing operation we can achieve the cropping of the image region
"""
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the file")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original",image)
cropped=image[100:300,100:400]
cv2.imshow("Cropped",cropped)
cv2.waitKey(0)

"""
    Contours:
    >contours are simply the outlines of an object in an image, If the image is simple enough, we might be able to get
    away with using the grayscale image as an input.
    >But for more complicated images, we must first find the object by using methods such as edge detection or thresholding
    we are simply seeking a binary image where white pixels correspond to objects in an image and black pixels as the
    background. There are many ways to obtain a binary image like this, but the most used methods are edge detection
    and thresholding
    >Key takeaway: For better accuracy you’ll normally want to utilize a binary image rather than a grayscale image
Finding and drawing contours:
    Untill now whatever we have learned we are succesfully able thresold , blur , find teh edge/outline of the object
    but how to find and access these outlines?
    by using Contours we can access these outlines
    In this Chapter out main Objectives would be :
     1> Find and detect the contour of objects in an image
     2>Extracting objects from the images using contours, mask and cropping

    Methods: To find the Contours:
    cv2.findContours(image, mode, method, contours, hierarchy, offset)
    >image: we should always copy the image that we are sending to the method as it will change that image so we should
            use image.copy()
    >mode: To specify the mode of retrieval of the contours ex(cv2.RETR_LIST--> Returns all the contours,externals as
            well as internal, or cv2.RETR_EXTERNAL--> To retrieve only the external contours)'
    >Method: we mostly use cv2.CHAIN_APPROX_SIMPLE to return all the contours, if we use CHAIN_APPROX_NONE we will store
    each and every (x,y) Coordinates which is not advisable.

    >function returns a tuple of values. The first value is the image itself for OpenCV 3 (OpenCV 2.4 and OpenCV 4
    do not place the image in the first value of the tuple)
    >The 2nd value is the contours themselves for OpenCV 3 (for OpenCV 2.4 OpenCV 4, it is first value).
    These contours are simply the boundary points of the outline along the object
    >The third value is the hierarchy of the contours (for OpenCV 2.4 and OpenCV 4, it is the second value)
    --->we should be carefull while using this methods because different version of opencv will give different results


"""

import argparse
import cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image",image)

(image, cnts, hst)=cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))

# show the output image
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

# loop over the contours individually and draw each of them
for (i, c) in enumerate(cnts):
    print("Drawing contour #{}".format(i + 1))
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Single Contour", clone)
    cv2.waitKey(0)
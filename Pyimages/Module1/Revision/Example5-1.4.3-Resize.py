"""
Resize is a tricky task as we always need to take care of the Aspect ratio or else the image might
resize but it will look distorted (Aspect Ratio=Width/height)
2 Steps:
    1> Calculate the Ratio and the approperiate value of Height or width based on which ever is provided
    2> Apply cv2.resize(src, dsize, dst, fx, fy, interpolation) method there are many interpolation methods there

how resize actually happens is
1> when we have to reduce the size of the image then we take the nearby pixel values of a particular point and c
calculate the central pixel value based on that, generally when we decrease a size it not a problem, but on
increasing the size of the pixel we have to create new pixels so we need to be very accountable while choosing the
methods fo interpolation

Interpolation methods
these methods are actully resposible to find out what should be the value of a pixel based on sourrounding pixels
so it will itterate for each and every pixel in the image and calculate


Now Again as we see that it is a 2 step process so we have defined single method using wich we can just provide
the image , the interpolation method and the hieght or width on which we need to resize
"""
import argparse
import cv2
import numpy as np
import SimpleUtils
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the file ")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
(h,w)=image.shape[:2]
#calculating the  aspect Ratio
ar=w/h
#new Height according to which we need to resize
hnew=350
dim=(int(hnew*ar),hnew)

resized=cv2.resize(image, dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized based on the height", resized)
cv2.waitKey(0)


wnew=400
dim=(wnew,int(wnew*ar))
resized=cv2.resize(image, dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized based on the width", resized)
cv2.waitKey(0)


# using the Resize method defined in SimpleUtils class
resized=SimpleUtils.resize(image,height=500,inter=cv2.INTER_AREA)
cv2.imshow("Resized based on the height", resized)
cv2.waitKey(0)
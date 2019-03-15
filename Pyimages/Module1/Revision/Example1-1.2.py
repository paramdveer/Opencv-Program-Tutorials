"""
In this lesson we learn about 3 methods
cv2.imshow("<Name of the window that you want to show>",<image array>)
cv2.imread("<Path of the image file")
cv2.wait(0)-->to wait until the user presses a key
image.shape--> Return the size or dimesions of the image (height, width, number of channels)
to get only height and width (h,w)=image.shape[:2}
"""
import argparse
import numpy as np
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the Input image file")
args=vars(ap.parse_args())

# To read the image from the dist we use
#cv2.imread("Location of the file")
image=cv2.imread(args["image"])

#Getting the properties like height width of the image
(h,w)=image.shape[:2]
print("Height ={} : widht =:{}".format(h,w))

#Getting the values of the color at a particular location
(b,g,r)=image[0,0]
print("The bgr Value ar 0,0 is Blue:{}, Green:{}, red:{}".format(b,g,r))

#changing the pixel value at the particular location
image[0,0]=(255,0,255)
(b,g,r)=image[0,0]
print("The bgr Value ar 0,0 is Blue:{}, Green:{}, red:{}".format(b,g,r))

#Getting the part of the image using the umpy array slicing
#image[<Ystart:Yend>,<Xstart:xend>]
#getting the center location of the image
(cX, cY)=(w//2,h//2)
tl=image[0:cY,0:cX]
#displaying on ly the top left corner of the image
cv2.imshow("Top Left Corner",tl)
cv2.waitKey(0)
tr=image[0:cY,cX:w]
br=image[cY:h,cX:w]
bl=image[cY:h,0:cX]
cv2.imshow("top righ corner", tr)
cv2.waitKey(0)
cv2.imshow("Bottom left",bl)
cv2.waitKey(0)
cv2.imshow("Bottom Right",br)
cv2.waitKey(0)
#let us make the entire top right corner green
image[0:cY,cX:w]=(0,255,0)
cv2.imshow("Made Top Right Corner green",image)
cv2.waitKey(0)

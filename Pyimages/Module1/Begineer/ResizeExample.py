import argparse
import numpy as np
import cv2
import imutils

ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path Of the IMage")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
cv2.imshow("Original",image)

# Let Us calculate the Aspect ratio of the Image by dividing the width of new and old image
r=150.0/image.shape[1]
dim=(150,int(image.shape[0]*r))
resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized ON width",resized)
# Resizing based on height
r=100.0/image.shape[0]
dim=(int(image.shape[1]*r),100)
resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized ON Height",resized)

# Resizing with the help of Imutils
resized=imutils.resize(image,100)
cv2.imshow("Resized Based ON width with imutils",resized)
cv2.waitKey(0)

#REsizing withDifferent InterPolation method
methods=[("cv2.INTER_AREA",cv2.INTER_AREA),("cv2.INTER_LINEAR",cv2.INTER_LINEAR),("cv2.INTER_CUBIC",cv2.INTER_CUBIC),("cv2.INTER_AREA",cv2.INTER_AREA),("cv2.INTER_LANCZOS4",cv2.INTER_LANCZOS4)]
for (name,method) in methods:
    resized=imutils.resize(image,width=image.shape[1]*3,inter=method)
    cv2.imshow("Method:{}".format(name),resized)
    cv2.waitKey(0)
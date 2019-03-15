"""
Rotation is making a image rotate about a point which may not be centre also
we achieve rotation by creating a rotation matrix
2 steps :
1>  First define the Rotation Matrix
        M=cv2.getRotationMatrix2D(center, Angle, scale)
            center=the center can be any point
            Angle=Angle in degress of Counter lock wise rotation
            scale=1.0=same size, 2.0 double the size, .5= half the size
2>  Apply the warpAffine mathod to apply the matrix
        cv2.warpAffine(image, M, Dsize, dst, flag, border mode , border Value)


"""
import cv2
import numpy as np
import SimpleUtils
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path of the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
(cX,cY)=(image.shape[1]//2,image.shape[0]//2)
M=cv2.getRotationMatrix2D((cX,cY),45,2.0)
Rotated=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Rotated by 45 degrees",Rotated)
cv2.waitKey(0)

# Rotation using the Simpleutils methods
Rotated=SimpleUtils.rotate(image,90,(cX,cY))
cv2.imshow("Rotated by 90 degree", Rotated)
cv2.waitKey(0)
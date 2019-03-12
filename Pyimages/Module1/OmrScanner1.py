import argparse
import cv2
import imutils
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the Answer Sheet")
args=vars(ap.parse_args())
def crop(path):
    image=cv2.imread(path)
    cv2.imshow("Original Image",image)
    (h,w)=image.shape[:2]
    Cy1=int(0.25*h)
    Cy2=int(0.35*h)
    Cx1=int(0.78*w)
    Cx2=int(0.95*w)
    image2=image[Cy1:Cy2,Cx1:Cx2]
    cv2.imshow("Cropped Image",image2)
    #cv2.waitKey(0)
    r=image2.shape[0]*.75/image2.shape[0]
    dim=(int(image2.shape[1]*r),int(image2.shape[0]*.75))
    image3=cv2.resize(image2,dim,interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized",image3)
    #cv2.waitKey(0)
    return image3



import argparse
import cv2
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args=vars(ap.parse_args())

def autoEdge(image,sigma=0.33):
    # calcluate the median of the image
    v=np.median(image)
    #calcluate the upper and the lower limit of thresold values
    lower=int(max(0,(1-sigma)*v))
    upper=int(min(255,(1-sigma)*v))
    edge=cv2.Canny(image,lower,upper)
    return edge

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Original",image)
cv2.imshow("GrayScale",gray)
cv2.imshow("Blurred",blur)
cv2.waitKey(0)

wide=cv2.Canny(blur,10,200)
tight=cv2.Canny(blur,230,250)
auto=autoEdge(blur)
cv2.imshow("Wide",wide)
cv2.waitKey(0)
cv2.imshow("tight",tight)
cv2.waitKey(0)
cv2.imshow("auto",auto)
cv2.waitKey(0)
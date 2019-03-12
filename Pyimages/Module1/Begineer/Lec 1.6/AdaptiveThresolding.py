#from skimage.filters import thresold_local
import argparse
import cv2
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Origninal",image)
cv2.waitKey(0)

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.imshow("Blurred",blurred)
cv2.waitKey(0)


thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,15)
cv2.imshow("Open Cv Thresold Image",thresh)
cv2.waitKey(0)

#T=thresold_local(blurred,29,offset=5,method="gaussian")
#thresh=(blurred<T).astype("uint8")*255
#cv2.imshow("Sckimage Thresolding",thresh)
#cv2.waitKey(0)
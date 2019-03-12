import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)

cv2.imshow("Original",image)
cv2.imshow("Blurred",blurred)
# Applying the canny Edge Detection

#having the wide range of thresold values
wide=cv2.Canny(blurred,10,200)
#having mid range thresold values
mid=cv2.Canny(blurred,40,150)
# Having the Narrow or tight Range values
tight=cv2.Canny(blurred,240,250)

cv2.imshow("Wide",wide)
cv2.waitKey(0)
cv2.imshow("Mid",mid)
cv2.waitKey(0)
cv2.imshow("Tight",tight)
cv2.waitKey(0)

import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path TO the IMage")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(7,7),0)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.imshow("Blurred",blurred)

cv2.waitKey(0)
(T,threshInv)=cv2.threshold(blurred,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold",threshInv)

print("Threshold value :{}".format(T))
masked=cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("MAsked Result", masked)
cv2.waitKey(0)
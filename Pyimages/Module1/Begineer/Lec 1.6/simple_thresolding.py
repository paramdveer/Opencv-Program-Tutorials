import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path TO the file")
args=vars(ap.parse_args())

#converting image to gray and blurred using a kernel of (7,7)
image=cv2.imread(args["image"])
cv2.imshow("Original Image",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(7,7),0)
cv2.waitKey(0)
cv2.imshow("Blurred",blurred)
cv2.imshow("Gray",gray)
#applying thresold to get the thressold image of the blurred image
#cv2,threshold() return 2 values T=threshold value, thresh= thresold image it return the tuple of two
#We are applying inverse thresolding
(T,threshinv)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresold inverse ", threshinv)
cv2.waitKey(0)
#We are applying inverse thresolding
(T,thresh)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)
cv2.imshow("thresold ", thresh)
cv2.waitKey(0)
# Using bitwise and operation to mask the thresold image over original image
maskedimg=cv2.bitwise_and(image,image,mask=threshinv)
cv2.imshow("MAsked with inverese thresolding",maskedimg)
cv2.waitKey(0)
maskedimg=cv2.bitwise_and(image,image,mask=thresh)
cv2.imshow("MAsked with thresolding",maskedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


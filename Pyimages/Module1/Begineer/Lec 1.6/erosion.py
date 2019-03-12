import numpy as np
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("GetyScale",grey)

#Erosion Operation
for i in range(0,3):
    eroded=cv2.erode(grey,None,iterations=i+1)
    cv2.imshow("Eroded {} times".format(i+1),eroded)
    cv2.waitKey(0)

#Dilation Opreation
for i in range(0,3):
    dilated=cv2.dilate(grey,None,iterations=i+1)
    cv2.imshow("Eroded {} times".format(i+1),dilated)
    cv2.waitKey(0)


#Opening Operation Erosion --> Dilation
cv2.destroyAllWindows()
kernelSizes=[(3,3),(5,5),(7,7)]
cv2.imshow("Original",image)
for kernelSize in kernelSizes:
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelSize)
    opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
    cv2.imshow("Opneing {} {}".format(kernelSize[0],kernelSize[1]),opening)
    cv2.waitKey(0)

#Closing Opreation dilation-> erosion
cv2.destroyAllWindows()
for kernelSize in kernelSizes:
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelSize)
    closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("closing {} {}".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

#Gradient = Dilation-Erosion=Outline
cv2.destroyAllWindows()
for kernelSize in kernelSizes:
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernelSize)
    gradient=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
    cv2.imshow("closing {} {}".format(kernelSize[0], kernelSize[1]),gradient)
    cv2.waitKey(0)
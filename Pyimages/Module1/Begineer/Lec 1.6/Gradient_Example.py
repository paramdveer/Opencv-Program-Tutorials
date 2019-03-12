import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the Image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#Computing gradient along X,Y direction
gX=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=1,dy=0)
gY=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=0,dy=1)
#the above methods returns a floating value so we have to convert it to 8-bit unsigned int
gX=cv2.convertScaleAbs(gX)
gY=cv2.convertScaleAbs(gY)
# Display the individual gradients
cv2.imshow("Sobel-X",gX)
cv2.waitKey(0)
cv2.imshow("Sobel-Y",gY)
cv2.waitKey(0)

# Combine the above gradients in equal ratios
combined=cv2.addWeighted(gX,0.5,gY,0.5,0)
cv2.imshow("COmbined",combined)
cv2.waitKey(0)

np.wh
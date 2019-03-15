"""
Translation is the process of shifting th image along the x or y axis or both
first we nee to define a matrix
M=np.float31([[1,0,shift-X],[0,1,shift-Y]])
cv2.warpAffine(<src>, M, dsize, dst, flag, border mode , border Value)
using the above apprach we can shift the image along x or y axis
for simplicity we will define out own translate funtion for using in out project
NOTE: the above function will not change the original src image we migh provide the desination image in seperate argument

we have defined out own function which we can use to translate an imagess
"""
import cv2
import argparse
import numpy as np
import SimpleUtils
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image file")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
# now, let's shift the image 50 pixels to the left and 90 pixels up, we
# accomplish this using negative values
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)
shifted=SimpleUtils.translate(image,0,40)
cv2.imshow("Shifted down", shifted)
cv2.waitKey(0)
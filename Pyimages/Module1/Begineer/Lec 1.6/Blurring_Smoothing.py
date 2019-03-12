import argparse
import numpy as np
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the Input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original Image",image)
kernelsizes=[(3,3),(7,7),(9,9)]

for ksize in kernelsizes:
    blur=cv2.blur(image,ksize)
    cv2.imshow("Averaging({}{})".format(ksize[0],ksize[1]),blur)
    cv2.waitKey(0)
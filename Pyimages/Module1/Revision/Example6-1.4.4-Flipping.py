"""
Flipping the image vertically or hirizontally or both
cv2.flip(<image>, Code,<destination>)
Code:
    0------vertically: along the x-axis-0
    1------horizontally:along the y-axis 1
    2------horizontally+vertically: -1
"""
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the file")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
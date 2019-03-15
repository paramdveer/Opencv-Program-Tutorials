"""
Splitting and merging the channel
As we know the image has multiple channels (Red, Green, Blue)
till now we know about the Grayscale and binary image, now we will know how to access the individual (Blue,Green, Red)
channels
It can be achieved in multiple ways , using array slicing also but we will focus on
cv2.split() and cv2.merge() methods
why do we need splitting an image int he multiple channels?
When you investigate each channel individually rather than as a whole, you can visualize how much each channel
contributes to the overall output image.
Performing this exercise is extremely helpful, especially when you are applying methods such as thresholding and edge
detection.
when we spilt and display each channel individually we see grayscale type of image
so to see it in color image we can use cv2.merge() method
zeros=np.zeros(image.shape[:2],dtype:"uint8")
cv2.merge([zeros,zeros,R])
"""
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype = "uint8")
"""we construct a NumPy array of zeros, with the same width and height as our original image. T
hen, in order to construct the Red channel representation of the image, we make a call to cv2.merge , 
but specifying our zeros  array for the Green and Blue channels"""
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
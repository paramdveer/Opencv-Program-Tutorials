"""
Image Arithmetic:
1>The Addtion and Substraction of the images
2> the Difference in the Addtion and substraction of open cv and numpy addition and Substraction
clipping>
    In Clipping there is a maximum value and a minumum value if during any operation substraction or addition the value
    falls outside of the boundaries it will take the minimum and maximum value go the boundaries
    ex limit of colors or uint8 are 0-256 so if we add cv2.add(np.uint8([200]),np.uint8([100]))==250
    cv2.subtract(np.uint8([100]),np.uint8([200]))==0
    the limit of uint is 0-255 so
    100+200=300 but as limit is 255 so output is 255
    200-100=-100 but as limit is 0 so output is 0
modulo arithmetic //“wraps around.
In Wrap around if we have a maximum and minimum value, if during any operatino substraction or addition the value
falls outside of the range it will wrap the values again within the boundaries
ex the limit of the colors or uint8 is 0-255 so id we add (np.uint8([200]) + np.uint8([100]))==44
(np.uint8([100]) + np.uint8([200]))=155
100+200=300 but here max=255 so after 255 again it starts from 0 so 45
200-100=-100 but here min is 0 so it wil count backwards from 255==155

To increase the brightness we can add pixels to the image
To decrease the brightness we can substract the pixels to the image


"""
# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# images are NumPy arrays, stored as unsigned 8 bit integers -- this
# implies that the values of our pixels will be in the range [0, 255]; when
# using functions like cv2.add and cv2.subtract, values will be clipped
# to this range, even if the added or subtracted values fall outside the
# range of [0, 255]. Check out an example:
print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))

# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulo (wrap around) instead of being  clipped to the [0, 255]
# range. This is important to keep in mind when working with images.
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

# let's increase the intensity of all pixels in our image by 100 -- we
# accomplish this by constructing a NumPy array that is the same size of
# our matrix (filled with ones) and the multiplying it by 100 to create an
# array filled with 100's, then we simply add the images together; notice
# how the image is "brighter"
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

# similarly, we can subtract 50 from all pixels in our image and make it
# darker
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
"""
NOTE:
    Up until this point we have only applied morphological operations to binary images.
    But we can also apply morphological operations to grayscale images as well. In fact, both the top hat/white hat and
    the black hat operators are more suited for grayscale images rather than binary ones.
6_____________Top Hat/White Hat____________:
    the difference between the original (grayscale/single channel) input image and the opening.
    A top hat operation is used to reveal bright regions of an image on dark backgrounds
    We will use the cv2.MORP_TOPHAT as the morphological gradient
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
    we need to select the structuring element based upen the object which we want to select suppose its a number plate
    then defines a rectangular structuring element with a width of 13 pixels and a height of 5 pixels.
    As I mentioned earlier in this lesson, structuring elements can be of arbitrary size. And in this case,
    we are applying a rectangular element that is almost 3x wider than it is tall.
    By having some basic a priori knowledge of the objects you want to detect in images, we can construct structuring
    elements to better aide us in finding them
7________________Black Hat__________________:
    The black hat operation is the difference between the closing of the input image and the input image itself.
    the black hat operator is simply the opposite of the white hat operator
    We apply the black hat operator to reveal dark regions (i.e. the license plate text) against light backgrounds
    (i.e. the license plate itself).
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    here we use cv2.MORPH_BLACKHAT as the morphological gradient

"""
# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# construct a rectangular kernel and apply a blackhat operation which
# enables us to find dark regions on a light background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will enable
# us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
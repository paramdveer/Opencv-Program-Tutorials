"""
Objectives:
    Define what an image gradient is.
    Compute changes in direction of an input image.
    Define both gradient magnitude and gradient orientation.
    Learn how to compute gradient magnitude and gradient orientation.
    Approximate the image gradient using Sobel and Scharr kernels.
    Learn how to use the cv2.Sobel  function to compute image gradient representations in OpenCV.

Gradients:
    >The image gradient is one of the fundamental building blocks in computer vision image processing,
    >We use gradients for detecting edges in images, which allows us to find contours and outlines of objects in images,
    >The main application of image gradients lies within edge detection
    >Image gradient is defined as a directional change in image intensity.
    >At each pixel of the input (grayscale) image, a gradient measures the change in pixel intensity in a given direction
    .By estimating the direction or orientation along with the magnitude (i.e. how strong the change in direction is),
    we are able to detect regions of an image that look like edges
    Gradient magnitude and Gradient orientation.
    Gy = I(x, y + 1) - I(x, y - 1)
    Gx = I(x + 1, y) - I(x - 1, y)
    gradient magnitude:
        measure how strong the change in image intensity is. The gradient magnitude is a real-valued number that
        quantifies the “strength” of the change in intensity.
        G = (Gx^2+Gy^2)^(1/2)
    Gradient orientation:
        in which direction the change in intensity is pointing. As the name suggests, the gradient orientation will give
         us an angle or \theta that we can use to quantify the direction of the change
         degree= arctan2(Gy,Gx)*(180/3.14)


    Sobel and Scharr kernels:



"""
# import the necessary packages
import argparse
import numpy as np
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-l", "--lower-angle", type=float, default=175.0,help="Lower orientation angle")
ap.add_argument("-u", "--upper-angle", type=float, default=180.0,help="Upper orientation angle")
args = vars(ap.parse_args())


# load the image, convert it to grayscale, and display the original
# image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# the `gX` and `gY` images are now of the floating point data type,
# so we need to take care to convert them back to an unsigned 8-bit
# integer representation so other OpenCV functions can utilize them
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the sobel X and Y representations into a single image
sobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

# show our output images
cv2.imshow("Sobel X", gX)
cv2.imshow("Sobel Y", gY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# compute the gradient magnitude and orientation respectively
mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# find all pixels that are within the upper and low angle boundaries
idxs = np.where(orientation >= args["lower_angle"], orientation, -1)
idxs = np.where(orientation <= args["upper_angle"], idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs > -1] = 255

# show the images
cv2.imshow("Mask", mask)
cv2.waitKey(0)
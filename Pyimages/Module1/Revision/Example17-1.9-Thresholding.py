"""
Thresholding:
    Thresholding is one of the most common (and basic) segmentation techniques in computer vision and it allows us to
    separate the foreground (i.e. the objects that we are interested in) from the background of the image.
    Thresholding is the binarization of an image. In general, we seek to convert a grayscale image to a binary image,
    where the pixels are either 0 or 255.
    A simple thresholding example would be selecting a threshold value T, and then setting all pixel intensities less
    than T to zero, and all pixel values greater than T to 255. In this way, we are able to create a binary
    representation of the image
cv2.threshold(src, ThreshValue, MaxValue, type, dst)
    src-> Input image must be a grayscalle image and if it is blurred apperoperiatly it gives better result
    ThreshValue: the T value for which any pixel <T set to 0, and any pixel > T set to the MAxvalue,
    MaxValue: The maximum for the binary image
    tpe: The method to be followed to do thresholding
    cv2.THRESH_BINARY_INV  method, which indicates that pixel values p less than T are set to the output(MaxValue) value
    cv2.THRESH_BINARY method, which indicates that pixel valies p  more than T as set to the output(MaxValue)\
    =================cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV/cv2.THRESH_BINARY)=====================
    This function return two things, 1> the ThreshValue, and 2>the output image,
    except in case of simple thresholding we will not specify the value of Thresh so in that case we need to know the T val.

Simple Thresholding:
    Applying simple thresholding methods requires human intervention. We must specify a threshold value T.
    All pixel intensities below T are set to 255. And all pixel intensities greater than T are set to 0
    We could also apply the inverse of this binarization by setting all pixels greater than T to 255 and all pixel
    intensities below T to 0
    =================cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV/cv2.THRESH_BINARY)=====================
    In Simple thresholding we suppy the threshold value manually, so the threshold value working perfectly for one image
    may not work accurately for other images so it should be generated dynamically and automatically

    due to this draw back we opencv2 came up with the other thresolding type
    For simple images in controlled lighting conditions, it might be feasible for us to hardcode this value.
    But in real-world conditions where we do not have any a priori knowledge of the lighting conditions,
    we actually automatically compute an optimal value of T using Otsu’s method

Otsu’s Method:
    Otsu’s method assumes that our image contains two classes of pixels: the background and the foreground.
    Furthermore, Otsu’s method makes the assumption that the grayscale histogram of our pixel intensities of our image
    is bi-modal, which simply means that the histogram is two peaks.
    Based on the grayscale histogram, Otsu’s method then computes an optimal threshold value T such that the variance
    between the background and foreground peaks is minimal.
    However, Otsu’s method has no a priori knowledge of what pixels belong to the foreground and which pixels belong to
    the background — it’s simply trying to optimally separate the peaks of the histogram
    It’s also important to note that Otsu’s method is an example of global thresholding — implying that a single value
    of T is computed for the entire image
    cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    --> int the ThreshValue parameter we are passing 0 as the value will be generated automatically by OTSU method
    -->in the type parameter of the thresold method we pass cv2.THRESH_OTSU

    cv2.threshold  function will again return a tuple of 2 values for us: the threshold value T and the thresholded
    image itself, in previous case we knew the value of T but in this case we need to get the value of threshold so it
    returns that.


    But this value is optimal in the sense that it does the best possible job to split the foreground and the background
    assuming a bi-modal distribution of grayscale pixel values
    f the grayscale image does not follow a bi-modal distribution, then Otsu’s method will still run, but it may not
    give us our intended results.In that case, we will have to try adaptive thresholding.

    NOTE:
        Otsu’s method is a global thresholding method. In situations where lighting conditions are semi-stable and the
        objects we want to segment have sufficient contrast from the background, we might be able to get away with
        Otsu’s method.
        But when the lighting conditions are non-uniform — such as when different parts of the image are illuminated
        more than others, we can run into some serious problem. And when that’s the case, we’ll need to rely on adaptive
        thresholding.
"""

import cv2
import argparse
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)

# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is our threshold check
# if a pixel value is greater than our threshold (in this case,
# 200), we set it to be BLACK, otherwise it is WHITE.
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.waitKey(0)
# using normal thresholding (rather than inverse thresholding),
# we can change the last argument in the function to make the coins
# black rather than white.
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)
# finally, we can visualize only the masked regions in the image
cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply Otsu's automatic thresholding -- Otsu's method automatically
# determines the best threshold value `T` for us
(T, threshInv) = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("Otsu's thresholding value: {}".format(T))

# finally, we can visualize only the masked regions in the image
cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
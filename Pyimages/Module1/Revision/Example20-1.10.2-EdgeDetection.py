"""
Edge detection:
    The Canny edge detector:
      The Canny edge detector is a multi-step algorithm used to detect a wide range of edges in images.
      The algorithm itself was introduced by John F. Canny in his 1986 paper, A Computational Approach To Edge Detection
      Canny edge detector is also a building block for methods such as object detection in images. Whether we are
      finding the distance from our camera to an object, building a mobile document scanner, or finding a Game Boy
      screen in an image,
      Edge:
      Edge is defined as discontinuities in pixel intensity, or more simply, a sharp difference and change in pixel values
    We should always parse a GrayScale image for the edge detection
    Canny edge detection algorithm, which is a multi-step process:

        1>Applying Gaussian smoothing to the image to help reduce noise.
        2>Computing the G_{x} and G_{y} image gradients using the Sobel kernel.
        3>Applying non-maxima suppression to keep only the local maxima of gradient magnitude pixels that are pointing
        in the direction of the gradient.
        4>Defining and applying the T_{upper} and T_{lower} thresholds for Hysteresis thresholding.

        Step 1: Gaussian smoothing:
            >smoothing and blurring, smoothing an image allows us to ignore much of the detail and instead focus on the
            actual structure.
            >This also makes sense in the context of edge detection — we are not interested in the actual detail of the
            image. Instead, we want to apply edge detection to find the structure and outline of the objects in the
            image so we can further process them.

        Step 2: Gradient orientation and magnitude:
            >compute the gradient orientation and magnitude
            >as we have seen, the gradient magnitude is quite susceptible to noise and does not make for the best edge
            detector. We need to add two more steps on to the process to extract better edges

        Step 3: Non-maxima Suppression:(edge thinning Process)
            >the edges themselves are still quite noisy and blurred, but in reality there should only be one edge
            response for a given region, not a whole clump of pixels reporting themselves as edges.
            >To apply non-maxima suppression we need to examine the gradient magnitude G and orientation at each pixel and then
                1>Compare the current pixel to the 3 times 3 neighborhood surrounding it.
                2>Determine in which direction the orientation is pointing:
                    1>If it’s pointing towards the north or south, then examine the north and south magnitude.
                    1>If the orientation is pointing towards the east or west, then examine the east and west pixels.
                3>If the center pixel magnitude is greater than both the pixels it is being compared to, then preserve
                    the magnitude. Otherwise, discard it.
        Step 4: Hysteresis thresholding:
            >Even after applying non-maxima suppression, we may need to remove regions of an image that are not
            technically edges, but still responded as edges after computing the gradient magnitude and applying
            non-maximum suppression.
            >To ignore these regions of an image, we need to define two thresholds: T_{upper} and T_{lower}
                1>Any gradient value G > T_{upper}  is sure to be an edge.
                2>Any gradient value G < T_{lower} is definitely not an edge, so immediately discard these regions.
                3>And any gradient value that falls into the range T_{lower} < G < T_{upper} needs to undergo additional tests:
                    1>if the particular gradient value is connected to a strong edge (i.e. G > T_{upper}), then mark the
                    pixel as an edge
                    2>If the gradient pixel is not connected to a strong edge, then discard it.
                Setting these threshold ranges is not always a trivial process.
                1>If the threshold range is too wide then we’ll get many false edges instead of being about to find
                just the structure and outline of an object in an image
                2>Similarly, if the threshold range is too tight, we won’t find many edges at all and could be at
                risk of missing the structure/outline of the object entirely
                So we will learn how to automatically tune the Thresold upper and lower values.
       Method= cv2.Canny(image, threshold-Lower, threshold-upper, edges, aperturesize, L2Gradient)
       threshold-Lower=T{Lower}
       threshold-upper=T{Upper}

       Now as we could see that everytime we need to provide the upper and lower threshold values manually so this can
       also be automated, moreover each image we should have a different set of values


    Automatically tuning edge detection parameters:
    What are the optimal values for the thresholds?
    This question is especially important when you are processing multiple images with different contents captured under
    varying lighting conditions

    Algorithm to determine automatically a reliable Threshold limits:
    def auto_canny(image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper)

        # return the edged image
        return edged
    >We start by defining our auto_canny  function. This function requires a single argument, image , which is the
    single-channel image that we want to detect images in. An optional argument, sigma , can be used to vary the
    percentage thresholds that are determined based on simple statistics.
    >Next up, we compute the median of the pixel intensities in the image. Unlike the mean, the median is less sensitive
    to outlier pixel values inside the image, thus making it a more stable and reliable statistic for automatically
    tuning threshold values
    >We then take this median value and construct two thresholds, lower  and upper . These thresholds are constructed
    based on the +/- percentages controlled by the sigma  argument
    >A lower value of sigma  indicates a tighter threshold, whereas a larger value of sigma  gives a wider threshold.
    In general, you will not have to change this sigma  value often. Simply select a single, default sigma  value and
    apply it to your entire dataset of images.
    >Note: In practice, sigma=0.33  tends to give good results on most of the dataset

    using the Above algorithm and methods we can mostly detect the edges of the image automatically

"""

import argparse
import cv2
import numpy as np


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the Image")
args=vars(ap.parse_args())

#loading the image and converting it into the grayscale and then blurring it to reduce the data
image=cv2.imread(args['image'])
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)

#showing the original and the blurred image
cv2.imshow("Original",image)
cv2.waitKey(0)
cv2.imshow("Blurred",blurred)
cv2.waitKey(0)
# Computing wide mid range and tight threshold for edges
wide=cv2.Canny(blurred,10,200)
mid=cv2.Canny(blurred,50,150)
tight=cv2.Canny(blurred, 225,250)

#Showing the Edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)

auto = auto_canny(blurred)

# show the images
cv2.imshow("Auto", auto)
cv2.waitKey(0)
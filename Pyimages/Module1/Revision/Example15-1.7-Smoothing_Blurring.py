"""
SMOOTHING and BLURRING
BLURRING:
    It’s what happens when your camera takes a picture out of focus. Sharper regions in the image lose their detail
    The goal here is to use a low-pass filter to reduce the amount of noise and detail in an image.
    ractically, this means that each pixel in the image is mixed in with its surrounding pixel intensities.
    This “mixture” of pixels in a neighborhood becomes our blurred pixel
     it’s actually quite helpful when performing image processing tasks,(It is most common pre processing task in the
     Computer Vision and image processing)

SMOOTHING:
    By smoothing an image prior to applying techniques such as edge detection or thresholding we are able to reduce
    the amount of high frequency content, such as noise and edges.
    This allows us to focus on the larger structural objects in the image

(averaging, Gaussian blurring, median filtering, bilateral filtering)
Averaging:
    It is an blurring operation
    takes an area of pixels surrounding a central pixel, averages all these pixels together,
    and replaces the central pixel with the average.
    By taking the average of the region surrounding a pixel, we are smoothing it and replacing it with the value of its
    local neighborhood. This allows us to reduce noise and the level of detail
    To accomplish our average blur, we’ll actually be convolving our image with a M \times N normalized filter where
    both M and N are both odd integers.
    As the size of the kernel increases, so will the amount in which the image is blurred.
    The larger your smoothing kernel is, the more blurred your image will look.

    =======cv2.blur(image, kernalSize, dst, anchor, bordertype)============
    kernal size: as we go on increasing the size of the kernel the more blurred the image is , we pass the size as (3,3)
    (5,5) and so on
    As the size of your kernel increases, your image will become progressively more blurred.
    This could easily lead to a point where you lose the edges of important structural objects in the image.
    Choosing the right amount of smoothing is critical when developing your own computer vision applications

Gaussian:
    Gaussian blurring is similar to average blurring, but instead of using a simple mean, we are now using a weighted mean
    Here neighborhood pixels that are closer to the central pixel contribute more “weight” to the average
    Gaussian smoothing is used to remove noise that approximately follows a Gaussian distribution.
    The end result is that our image is less blurred, but more naturally blurred,
    than using the average method discussed in the previous section
    ======cv2.GaussianBlur(<src>,kernelsize,sigmaX,dst,sigmaY,borderType)=================
    he first argument to the function is the image we want to blur.
    Secong argument is a tuple representing our kernel size
    The last parameter is our \sigma, the standard deviation of the Gaussian distribution. By setting this value to 0,
    we are instructing OpenCV to automatically compute \sigma based on our kernel size.
    In most cases, you’ll want to let your \sigma be computed for you, we can aslo provide our own sigma value

Int the above methods the kernal size could be any thing M*N(m and N could be any sam or diffferent odd integers)
But in below median blurring we will have kernals as K*K (here the kernal will not be rectangle rather a square)
Median:
    The median blur method has been most effective when removing salt-and-pepper noise
    (unlike the averaging method), instead of replacing the central pixel with the average of the neighborhood,
    we instead replace the central pixel with the median of the neighborhood.
    The reason median blurring is more effective at removing salt-and-pepper style noise from an image is that each
    central pixel is always replaced with a pixel intensity that exists in the image.
    And since the median is robust to outliers, the salt-and-pepper noise will be less influential to the median than
    another statistical method, such as the average
    ================cv2.medianBlur(image, ksize, dst)==========
    here we provide only one value of K as the matrix is k*K
    The median blur is by no means a “natural blur” like Gaussian smoothing. However, for damaged images or photos
    captured under highly sub-optimal conditions, a median blur can really help as a pre-processing step

Bilateral:
    Blurring methods so far have been to reduce noise and detail in an image; however, as a side effect we have tended
    to lose edges in the image
    n order to reduce noise while still maintaining edges, we can use bilateral blurring.
    Bilateral blurring accomplishes this by introducing two Gaussian distributions.
        1>The first Gaussian function only considers spatial neighbors.
          That is, pixels that appear close together in the (x, y)-coordinate space of the image
        2>The second Gaussian then models the pixel intensity of the neighborhood, ensuring that only pixels with
          similar intensity are included in the actual computation of the blur
    Intuitively, this makes sense. If pixels in the same (small) neighborhood have a similar pixel value,
    then they likely represent the same object.But if two pixels in the same neighborhood have contrasting values,
    then we could be examining the edge or boundary of an object — and we would like to preserve this edge.
    this method is able to preserve edges of an image, while still reducing noise. The largest downside to this method
    is that it is considerably slower than its averaging, Gaussian, and median blurring counterparts.
    ======cv.cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace,dst, border-Type)=========
        ->The first parameter we supply is the image we want to blur
        ->Then, we need to define the diameter of our pixel neighborhood — the larger this diameter is,
          the more pixels will be included in the blurring computation.Think of this parameter as a square kernel size
        ->The third argument is our color standard deviation, denoted as \sigma_{color}. A larger value for
           \sigma_{color} means that more colors in the neighborhood will be considered when computing the blur
        -> If we let \sigma_{color} get too large in respect to the diameter, then we essentially have broken the
           assumption  of bilateral filtering — that only pixels of similar color should contribute significantly to the blur.
        ->Finally, we need to supply the space standard deviation, which we call \sigma_{space},A larger value of \sigma
         {space} means that pixels farther out from the central pixel diameter will influence the blurring calculation
    This can be used as the preprocessing steps to get the edges of the figure
"""
import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args=vars(ap.parse_args())
#load the image, display it, and initialize the list of kernel sizes
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
# loop over the kernel sizes and apply an "average" blur to the image
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes and apply a "Gaussian" blur to the image
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes and apply a "Median" blur to the image
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original",image)
params=[(11,21,7),(11, 41, 21), (11, 61, 39)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
    # apply bilateral filtering and display the image
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
	title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)
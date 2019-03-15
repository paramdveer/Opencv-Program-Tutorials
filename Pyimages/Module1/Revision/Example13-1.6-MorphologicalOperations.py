"""
Morphological Operation:
Morphological operations are simple transformations applied to binary or grayscale images. More specifically, we apply
morphological operations to shapes and structures inside of images. We can use morphological operations to increase the
size of objects in images as well as decrease them. We can also utilize morphological operations to close gaps between
objects as well as open them
Morphological operations “probe” an image with a structuring element. This structuring element defines the neighborhood
to be examined around each pixel. And based on the given operation and the size of the structuring element we are able
to adjust our output image
Types:(Erosion, Dilation, Opening, Closing, Morphological gradient, Black hat, Top hat (or “White hat”))
Structuring Element:
Well, you can (conceptually) think of a structuring element as a type of kernel or mask. However, instead of applying
a convolution, we are only going to perform simple tests on the pixels.
---->cv2.getStructuringElement(Shape,Ksize,anchor=none)
     Shape:the save of the structuring element we want(cv2.MORPH_RECT,cv2.MORPH_CROSS,cv2.MORPH_ELLIPSE,etc)
     Ksize:size of the Structuring element we want to use

1_______Erosion________:
    Just like water rushing along a river bank erodes the soil, an erosion in an image “erodes”
    the foreground object and makes it smaller
    Erosion works by defining a structuring element and then sliding this structuring element from left-to-right and
    top-to-bottom across the input image
    A foreground pixel in the input image will be kept only if ALL pixels inside the structuring element are > 0.
    Otherwise, the pixels are set to 0 (i.e. background).
    Erosion is useful for removing small blobs in an image or disconnecting two connected objects.

    cv2.erode(src,kernel,dst,anchor,iteration, border-type, Border-Value)
    This function takes two required arguments and a third optional one,The first argument is the image that we want to erode
    The second argument to cv2.erode  is the structuring element. If this value is None , then a 3 \times 3 structuring
    element, identical to the 8-neighborhood structuring element will be used
    The last argument is the number of iterations  the erosion is going to be performed
    Erosions are most useful for removing small blobs from an image or disconnected two connected components
    erosion is performed in grayscale image/binary image to get better results
2__________Dilation__________:
    The opposite of an erosion is a dilation. Just like an erosion will eat away at the foreground pixels, a dilation
    will grow the foreground pixels.
    Dilations increase the size of foreground object and are especially useful for joining broken parts of an image together.
    Dilations, just as an erosion, also utilize structuring elements — a center pixel p of the structuring element is
    set to white if ANY pixel in the structuring element is > 0
    cv2.dilate(src,kernel,dst,anchor,iteration, border-type, Border-Value)
    Unlike an erosion where the foreground region is slowly eaten away at, a dilation actually grows our foreground region
    Dilations are especially useful when joining broken parts of an object
    it is used to connect two disconnecting blobs, Exactly opposite of the erosion
3.________Opening__________;
    An opening is an erosion followed by a dilation.
    Performing an opening operation allows us to remove small blobs from an image: first an erosion is applied to remove
    the small blobs, then a dilation is applied to regrow the size of the original object
    cv2.morphologyEx(src, op, kernel/Morphological Gradient,dst,anchor,iteration,border-type, border-value):
    her we pass op as cv.MORPH_OPEN
    This function is abstract in a sense — it allows us to pass in whichever morphological operation we want,
    followed by our kernel/structuring element.
    he first required argument of cv2.morphologyEx  is the image we want to apply the morphological operation to.
    The second argument is the actual type of morphological operation — in this case, it’s an opening operation.
    The last required argument is the kernel/structuring element that we are using
4.________Closing___________:
    The exact opposite to an opening would be a closing. A closing is a dilation followed by an erosion.
    Closing is used to close holes inside of objects or for connecting components together
    It can be done again using the same function cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

5_________Morphological Gradient___________:
    A morphological gradient is the difference between the dilation and erosion.
    It is useful for determining the outline of a particular object of an image
    we use the same above method cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

NOTE:
    Up until this point we have only applied morphological operations to binary images.
    But we can also apply morphological operations to grayscale images as well. In fact, both the top hat/white hat and
    the black hat operators are more suited for grayscale images rather than binary ones.
6_____________Top Hat/White Hat____________:
    the difference between the original (grayscale/single channel) input image and the opening.
    A top hat operation is used to reveal bright regions of an image on dark backgrounds

"""
import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GreyScale image",gray)

#Applying erosion
for i in range(0,3):
    eroded=cv2.erode(gray.copy(),None,iterations=i+1)
    cv2.imshow("Eroded #{}".format(i+1),eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original",image)
for i in range(0,3):
    dilated=cv2.dilate(gray.copy(),None,iterations=i+1)
    cv2.imshow("Dilated Image",dilated)
    cv2.waitKey(0)

# close all windows to cleanup the screen and initialize the list
# of kernels sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernels and apply a "closing" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernels and apply a "morphological gradient" operation
# to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)
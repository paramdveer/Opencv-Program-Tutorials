"""
Masking:
we can use a combination of both bitwise operations and masks to construct ROIs that are non-rectangular.
This allows us to extract regions from images that are of completely arbitrary shape
A mask allows us to focus only on the portions of the image that interests us
For example,
let’s say that we were building a computer vision system to recognize faces. The only part of the image we
are interested in finding and describing are the parts of the image that contain faces —
we simply don’t care about the rest of the content of the image.Provided that we could find the faces in the image,
we might construct a mask to show only the faces in the image

How to apply mask:
We use the combination of bitwise_and(src1,src2,dst,mask)
here we have to pass the original image in src1 and src2 so src1==src2
The first two parameters are the image itself (i.e., the images we want to apply the bitwise operation to).
However, the important part of this function is the mask  keyword. When supplied, the bitwise AND is True  when the
pixel values of the input images are equal and the mask is non-zero at each (x, y)-coordinate. In this case, only pixels
that are part of the white rectangle.

it will only display that part of the image where the coorinate value (x,y) mask is non zero and the src1 and src2 have
the same pixel value
how to create a mask:
we have to create a binary image with only the ROI masked as white pixel adn rest as zero which now we will do manually
but later we will make it automatic
"""
import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the source file")
args=vars(ap.parse_args())
# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Masking allows us to focus only on parts of an image that interest us.
# A mask is the same size as our image, but has only two pixel values,
# 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept. For example,
# let's construct a rectangular mask that displays only the person in
# the image
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Mask", mask)

# Apply our mask -- notice how only the person in the image is cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Now, let's make a circular mask with a radius of 100 pixels and apply the
# mask again
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
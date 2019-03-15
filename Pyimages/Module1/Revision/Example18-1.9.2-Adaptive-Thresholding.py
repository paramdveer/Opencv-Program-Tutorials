"""
Adaptive Thresholding:
    >For simple images with controlled lighting conditions, this usually isn’t a problem. But for situations when the
    lighting is non-uniform across the image, having only a single value of T can seriously hurt our thresholding performance
    >In order to overcome this problem, we can use adaptive thresholding, which considers small neighbors of pixels and
    then finds an optimal threshold value T for each neighbor. This method allows us to handle cases where there may
    be dramatic ranges of pixel intensities and the optimal value of T may change for different parts of the image
    >The general assumption that underlies all adaptive and local thresholding methods is that smaller regions of an
    image are more likely to have approximately uniform illumination. This implies that local regions of an image will
    have similar lighting, as opposed to the image as a whole, which may have dramatically different lighting for each region.
    >In adaptive thresholding, sometimes called local thresholding, our goal is to statistically examine the pixel
    intensity values in the neighborhood of a given pixel p.
    >choosing the size of the pixel neighborhood for local thresholding is absolutely crucial.
    >The neighborhood must be large enough to cover sufficient background and foreground pixels, otherwise the value of
    T will be more or less irrelevant
    >But f we make our neighborhood value too large, then we completely violate the assumption that local regions of an
    image will have approximately uniform illumination. Again, if we supply a very large neighborhood, then our results
     will look very similar to global thresholding using the simple thresholding or Otsu’s methods
    The general formula to compute T is thus:
    T = mean(I_{L}) - C
     cv2.adaptiveThreshold(src, MaxValue, adaptive method, threshold type. blocksize, c ,dst)
     adaptive method: method to compute the mean,(cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
     thresholdtype:cv2.THRESH_BINARY_INV/cv2.THRESH_BINARY
     blockSize:pixel neighborhood size
     C:constant C which I mentioned above — this value simply lets us fine tune our threshold value
"""
# import the necessary packages
from skimage.filters import threshold_local
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# instead of manually specifying the threshold value, we can use adaptive
# thresholding to examine neighborhoods of pixels and adaptively threshold
# each neighborhood -- in this example, we'll calculate the mean value
# of the neighborhood area of 25 pixels and threshold based on that value;
# finally, our constant C is subtracted from the mean calculation (in this
# case 15)
thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
cv2.imshow("OpenCV Mean Thresh", thresh)

# personally, I prefer the scikit-image adaptive thresholding, it just
# feels a lot more "Pythonic"
T = threshold_local(blurred, 29, offset=5, method="gaussian")
thresh = (blurred < T).astype("uint8") * 255
cv2.imshow("scikit-image Mean Thresh", thresh)
cv2.waitKey(0)
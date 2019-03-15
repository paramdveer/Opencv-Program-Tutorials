"""
Color-Space:
     color space is just a specific organization of colors that allow us to consistently represent and reproduce colors.
     A color model, on the other hand, is an abstract method of numerically representing colors in the color space.
     As we know, RGB pixels are represented as a 3-integer tuple of a Red, Green, and Blue value
     As a whole, a color space defines both the color model and the abstract mapping function used to define actual
     colors. Selecting a color space also informally implies that we are selecting the color model
     RGB, HSV, L*a*b*, and grayscale (which, again, is not technically a color space, but you’ll be using it in nearly
     all computer vision applications you develop)

RGB:
    o define a color in the RGB color model, all we need to do is define the amount of Red, Green, and Blue contained in
    a single pixel. Each Red, Green, and Blue channel can have values defined in the range [0, 255] (for a total of 256
    “shades”), where 0 indicates no representation and 255 demonstrates full representation.
    he RGB color space is an example of an additive color space: the more of each color is added, the brighter the pixel
     becomes and the closer it comes to white
     ince an RGB color is defined as a 3-valued tuple, with each value in the range [0, 255], we can thus think of the
     cube containing 256 x 256 x 256 = 16,777,216 possible colors

HSV:
    Hue: Which “pure” color we are examining. For example, all shadows and tones of the color “red” will have the same Hue.
    Saturation: How “white” the color is. A fully saturated color would be “pure,” as in “pure red.” And a color with
     zero saturation would be pure white.
    Value: The Value allows us to control the lightness of our color. A Value of zero would indicate pure black, whereas
     increasing the value would produce lighter colors.

L*a*b*:

    L-channel: The “lightness” of the pixel. This value goes up and down the vertical axis, white to black, with neutral
     grays at the center of the axis.
    a-channel: Originates from the center of the L-channel and defines pure green on one end of the spectrum and pure
     red on the other.
    b-channel: Also originates from the center of the L-channel, but is perpendicular to the a-channel. The b-channel
    defines pure blue at one of the spectrum and pure yellow at the other.

Grayscale:
    A grayscale representation of an image throws away the color information of an image and can also be done using the
    cv2.cvtColor  function


Notes:
    The grayscale representation of an image is often referred to as “black and white,” but this is not technically
    correct. Grayscale images are single channel images with pixel values in the range [0, 255] (i.e. 256 unique values).
    True black and white images are called binary images and thus only have two possible values: 0 or 255 (i.e. only 2
    unique values).
    Be careful when referring to grayscale image as black and white to avoid this ambiguity.
    However, converting an RGB image to grayscale is not as straightforward as you may think. Biologically, our eyes
    are more sensitive and thus perceive more green and red than blue.
    Thus when converting to grayscale, each RGB channel is not weighted uniformly, like this:
    Y = 0.333 \times R + 0.333 \times G + 0.333 \times B
    Instead, we weight each channel differently to account for how much color we perceive of each:
    Y = 0.299 \times R + 0.587 \times G + 0.114 \times B
    Again, due to the cones and receptors in our eyes, we are able to perceive nearly 2x the amount of green than red.
    And similarly, we notice over twice the amount of red than blue. Thus, we make sure to account for this when
     converting from RGB to grayscale.
    The grayscale representation of an image is often used when we have no use for color (such in detecting faces or
    building object classifiers where the color of the object does not matter). Discarding color thus allows us to save
    memory and be more computationally efficient.

    The key takeaway is to always consider your lighting conditions before you write a single line of code!
"""

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the original image and display it (RGB)
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)

# loop over each of the individual channels and display them
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the image to the HSV color space and show it
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# loop over each of the individual channels and display them
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the image to the L*a*b* color space and show it
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# loop over each of the individual channels and display them
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# show the original and grayscale versions of the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
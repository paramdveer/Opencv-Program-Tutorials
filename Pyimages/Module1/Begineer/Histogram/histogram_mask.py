import cv2
from matplotlib import pyplot as plt
import argparse
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)
def plot_histogram(image, title, mask=None):
    #grab the image channels initialize the tupple of colors and figure
    chans=cv2.split(image)
    colors=("b","g","r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    # Foop to loop over the channel
    for (color,chan) in zip(colors,chans):
        # create a histogram for the curent channel and plot it
        hist=cv2.calcHist([chan],[0],mask,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])


plot_histogram(image,"histogram of the original image")
#plt.close()
mask=np.zeros(image.shape[:2],dtype="uint8")
mask=cv2.rectangle(mask,(80,80),(200,200),255,-1)
cv2.imshow("mask",mask)
cv2.waitKey(0)
masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Applying the mask",masked)
cv2.waitKey(0)

plot_histogram(image,"Histogram of the masked image",mask=mask)
plt.show()
from skimage import measure
import numpy as np
import cv2
import argparse
from skimage.filters import threshold_local

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Image location of the plate")
args=vars(ap.parse_args())

plate=cv2.imread(args["image"])
#extract the Value component from the HSV color space and apply adaptive threshold
# to reveal the characters on the licence plate
V=cv2.split(cv2.cvtColor(plate,cv2.COLOR_BGR2HSV))[2]
cv2.imshow("Value Channel",V)
T=threshold_local(V,29,offset=15,method="gaussian")
thresh=(V<T).astype("uint8")*255

#Show the images
cv2.imshow("Lcience Plate",plate)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)

#Perform Connected Components analysison the thresholded Images and Initialize the
# mask to hold only the large components we are interested in
labels=measure.label(thresh,neighbors=8,background=0)
mask=np.zeros(thresh.shape,dtype="uint8")
print("[INFO] found {} blobs".format(len(np.unique(labels))))

for (i,label) in enumerate (np.unique(labels)):
    #if this is the background label, ignore it
    if label == 0:
        print("[INFO] label : 0 (background)")
        continue
    #otherwise construct the label mask to display only the connected components got the current label
    print("[INFO] label: {}(foreground)".format(i))
    labelMask=np.zeros(thresh.shape,dtype="uint8")
    labelMask[labels == label]=255
    numPixels=cv2.countNonZero(labelMask)

    # if the number of pixel in the component is considerably large ad it to our mask of large blobs
    if numPixels > 300 and numPixels <1500:
        mask=cv2.add(mask,labelMask)
    #show the label mask
    cv2.imshow("label",labelMask)
    cv2.waitKey(0)

#show the large components in the image
cv2.imshow("Large blobs", mask)
cv2.waitKey(0)
from matplotlib import pyplot as plt
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the file")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

chans=cv2.split(image)

colors=("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
#Loop over the channels
for (chan, color) in zip(chans, colors):
    #Create a histogram for the current channel and plot it
    hist=cv2.calcHist([chan],[0],None,[256],[0,256])
    #hist/=hist.sum()
    plt.plot(hist,color=color)
    plt.xlim([0,256])
plt.show()



# as 256 divisions a very much to examin we will dive it in 32 divisions
fig = plt.figure()
#creating a 2D color histogram for green and blue channel
ax=fig.add_subplot(131)
hist=cv2.calcHist([chans[0],chans[1]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

#creating a 2D color histogram for green and red channel
ax=fig.add_subplot(132)
hist=cv2.calcHist([chans[2],chans[1]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

#creating a 2D color histogram for Red and blue channel
ax=fig.add_subplot(133)
hist=cv2.calcHist([chans[0],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show()
#finally lets examine one of the 2D histograms
print("2D histogram shape: {}, with {} values".format(hist.shape,hist.flatten().shape[0]))
"""
hist=cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
print("3D histogram shape: {}, with {} values".format(hist.shape,hist.flatten().shape[0]))
plt.figure()
plt.axis("off")
plt.plot(cv2.cvtColor(hist,cv2.COLOR_BGR2RGB))
plt.show()
"""
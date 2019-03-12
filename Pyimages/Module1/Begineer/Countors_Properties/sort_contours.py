import numpy as np
import cv2

def sort_countours(cnts,method="left-to-right"):
    # initialise the reverse flag and sort index
    reverse=False
    i=0
    # handel if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse=True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i=1
    #construct the list of bounding boxes and sort them from top to bottom
    boundingboxes=[cv2.boundingRect(c) for c in cnts]
    (cnts, boundingboxes) = zip(*sorted(zip(cnts, boundingboxes), key=lambda b:b[1][i], reverse=reverse))

    #Return the list of sorted COntours and bounding boxes
    return (cnts, boundingboxes)


def draw_contours(image,c,i):
    #compute the center of the contour area and draw a circle representing the circle
    M=cv2.moments(c)
    cX=int(M["m10"]/M["m00"])
    cY=int(M["m01"]/M["m00"])

    #Draw the contour number on the image
    cv2.putText(image,"#{}".format(i+1),(cX-20,cY),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),2)
    #Return the image with the contour number drawn on it
    return image

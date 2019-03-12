import argparse
import cv2
import imutils
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
# to uncomment when Working in the same file
"""
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path To the Answer Sheet")
args=vars(ap.parse_args())
"""
def crop(path):
    image=cv2.imread(path)
    #cv2.imshow("Original Image",image)
    (h,w)=image.shape[:2]
    """
    Cy1=int(0.245*h)
    Cy2=int(0.35*h)
    Cx1=int(0.85*w)
    Cx2=int(0.99*w)
    """
    Cy1 = int(0.245 * h)
    Cy2 = int(0.30 * h)
    Cx1 = int(0.80 * w)
    Cx2 = int(0.94 * w)


    image2=image[Cy1:Cy2,Cx1:Cx2]
    #cv2.imshow("Cropped Image",image2)
    #cv2.waitKey(0)
    r=image2.shape[0]*.75/image2.shape[0]
    dim=(int(image2.shape[1]*r),int(image2.shape[0]*.75))
    image3=cv2.resize(image2,dim,interpolation=cv2.INTER_AREA)
    #cv2.imshow("Resized",image3)
    #cv2.waitKey(0)
    return image3


def masking(path):
    x_offset = y_offset = 25
    # l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    # image = cv2.imread(args["image"])

    image = crop(path)
    canvas = np.zeros((image.shape[0] + 50, image.shape[1] + 50, 3), dtype="uint8")
    # cv2.imshow("Blank image",canvas)
    # cv2.waitKey(0)
    canvas[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image;
    # cv2.imshow("Blank image",canvas)
    # cv2.waitKey(0)
    image = canvas
    # cv2.imshow("Original",image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("GreyScale",gray)
    # cv2.waitKey(0)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow("Blurred",blurred)
    # cv2.waitKey(0)
    edged = cv2.Canny(blurred, 75, 200)
    #cv2.imshow("Edged", edged)
    #cv2.waitKey(0)

    # ***********************************************************************************************

    # find contours in the edge map, then initialize
    # the contour that corresponds to the document
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None

    print(len(cnts))
    # ensure that at least one contour was found
    if len(cnts) > 0:
        # sort the contours according to their size in
        # descending order
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        # loop over the sorted contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # if our approximated contour has four points,
            # then we can assume we have found the paper
            if len(approx) == 4:
                docCnt = approx
                break

    # apply a four point perspective transform to both the
    # original image and grayscale image to obtain a top-down
    # birds eye view of the paper
    paper = four_point_transform(image, docCnt.reshape(4, 2))
    warped = four_point_transform(gray, docCnt.reshape(4, 2))
    # cv2.imshow("Paper",paper)
    # cv2.waitKey(0)
    #cv2.imshow("Wrapped", warped)
    #cv2.waitKey(0)

    # -------------------------------------------------------working file ----------------------
    # apply Otsu's thresholding method to binarize the warped
    # piece of paper
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cv2.imshow("Exam Thresold Image", thresh)
    cv2.waitKey(0)

    return thresh
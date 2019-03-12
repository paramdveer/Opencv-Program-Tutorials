from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
from imutils.perspective import four_point_transform
import OmrScanner1 as om
from ImageAlignment import alignImages
from ImageMatching import refResize
# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 1, 1: 0, 2: 0, 3: 1, 4: 1}


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,  help="path to the Ref image")
ap.add_argument("-r", "--test", required=True, help="path to test Image")
args = vars(ap.parse_args())
#----------------------------------Loading The Refrence Image and Alligning It-------------------
#im=cv2.imread("/home/paramveer/Downloads/images/Page3.jpeg")
im=cv2.imread(args["test"])

ref=cv2.imread(args["image"])
im=refResize(ref,im)

Exam,n=alignImages(im,ref)
cv2.imwrite("/home/paramveer/Downloads/images/test.jpeg",Exam)
print("test file Wtritten In /home/paramveer/Downloads/images/test.jpeg")
#-----------------------------------------end Of Allignment--------------------------------------


# load the image, convert it to grayscale, blur it
# slightly, then find edges
#s_img = cv2.imread("smaller_image.png")
#l_img = cv2.imread("larger_image.jpg")
x_offset=y_offset=25
#l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

#image = cv2.imread(args["image"])

image = om.crop(args["image"])
canvas=np.zeros((image.shape[0]+50,image.shape[1]+50,3),dtype="uint8")
#cv2.imshow("Blank image",canvas)
#cv2.waitKey(0)
canvas[y_offset:y_offset+image.shape[0],x_offset:x_offset+image.shape[1]]=image;
#cv2.imshow("Blank image",canvas)
#cv2.waitKey(0)
image=canvas
#cv2.imshow("Original",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("GreyScale",gray)
#cv2.waitKey(0)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow("Blurred",blurred)
#cv2.waitKey(0)
edged = cv2.Canny(blurred, 75, 200)
cv2.imshow("Edged",edged)
cv2.waitKey(0)

#***********************************************************************************************

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
#cv2.imshow("Paper",paper)
#cv2.waitKey(0)
cv2.imshow("Wrapped",warped)
cv2.waitKey(0)


#-------------------------------------------------------working fine ----------------------




#Same Code repated For testing-------------------------------------------------------------------------------
Exam=om.masking("/home/paramveer/Downloads/images/test.jpeg")
cv2.imshow("Marked Threshold Image",Exam)
cv2.imshow("unmarked Original Cropped Image",image)
cv2.waitKey(0)


# apply Otsu's thresholding method to binarize the warped
# piece of paper
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("threshHold Image",thresh)
cv2.waitKey(0)

# find contours in the thresholded image, then initialize
# the list of contours that correspond to questions
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
cnts = imutils.grab_contours(cnts)
questionCnts = []
print(len(cnts))

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour, then use the
    # bounding box to derive the aspect ratio
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)

    # in order to label the contour as a question, region
    # should be sufficiently wide, sufficiently tall, and
    # have an aspect ratio approximately equal to 1
    if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
        questionCnts.append(c)

print('Length Of Question count=',len(questionCnts))

# sort the question contours top-to-bottom, then initialize
# the total number of correct answers
questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
correct = 0

# each question has 5 possible answers, to loop over the
# question in batches of 5
# Fior 2 Questions
for (q, i) in enumerate(np.arange(0, len(questionCnts), 4)):
    # sort the contours for the current question from
    # left to right, then initialize the index of the
    # bubbled answer
    cnts = contours.sort_contours(questionCnts[i:i + 4])[0]
    bubbled = None

    # loop over the sorted contours
    for (j, c) in enumerate(cnts):
        # construct a mask that reveals only the current
        # "bubble" for the question
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        cv2.imshow("Counters with Mask",mask)
        cv2.waitKey(0)

        # apply the mask to the thresholded image, then
        # count the number of non-zero pixels in the
        # bubble area
        t1=cv2.countNonZero(mask)
        mask = cv2.bitwise_and(Exam, Exam, mask=mask)
        #mask=cv2.bitwise_and(thresh,thresh,mask=mask)
        total = cv2.countNonZero(mask)
        #t1=t1-total
        r=t1/total
        cv2.imshow("Counters with Mask and Mark",mask)
        print('total White pixels = ',total,": Total White Pixels in Mask = ",t1," : Ratio = ",r)

        cv2.waitKey(0)
        # if the current total has a larger number of total
        # non-zero pixels, then we are examining the currently
        # bubbled-in answer
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)
from __future__ import print_function
import cv2
import numpy as np
import argparse

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15


def alignImages(im1, im2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    cv2.imwrite("matches.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h
# to uncomment when Working in the same file
"""
if __name__ == '__main__':
    # Read reference image
    refFilename = "form.jpg"
    print("Reading reference image : ", refFilename)
    imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    imFilename = "scanned-form.jpg"
    print("Reading image to align : ", imFilename);
    im = cv2.imread(imFilename, cv2.IMREAD_COLOR)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h = alignImages(im, imReference)

    # Write aligned image to disk.
    outFilename = "aligned.jpg"
    print("Saving aligned image : ", outFilename);
    cv2.imwrite(outFilename, imReg)

    # Print estimated homography
    print("Estimated homography : \n", h)
"""


"""
ap= argparse.ArgumentParser()
ap.add_argument("-i","--ref",required=True,help="Path To Refference image")
ap.add_argument("-j","--test",required=True,help="Path TO the Test Image")
args=vars(ap.parse_args())
ref=cv2.imread(args["ref"], cv2.IMREAD_COLOR)
test=cv2.imread(args["test"], cv2.IMREAD_COLOR)
imReg, h = alignImages(test,ref)

w1=400/test.shape[1]
w2=400/imReg.shape[1]
w3=400/ref.shape[1]
ref=cv2.resize(ref,(400,int(w3*ref.shape[0])),interpolation=cv2.INTER_AREA)
test=cv2.resize(test,(400,int(w1*test.shape[0])),interpolation=cv2.INTER_AREA)
imReg=cv2.resize(imReg,(400,int(w2*imReg.shape[0])),interpolation=cv2.INTER_AREA)


print("Estimated homography : \n", h)
cv2.imshow("Refference Image",ref)
cv2.imshow("Original Image",test)
cv2.imshow("Alligned Image",imReg)
cv2.waitKey(0)
"""
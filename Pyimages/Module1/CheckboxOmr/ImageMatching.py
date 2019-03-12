import argparse
import cv2
import numpy as np

def refResize(ref,test):
    r = ref.shape[0]/test.shape[0]
    h1 = ref.shape[0]
    w1 = int(test.shape[1] * r)
    out = cv2.resize(test, (w1, h1), interpolation=cv2.INTER_AREA)
    return out
# to uncomment when Working in the same file
"""
ap=argparse.ArgumentParser()
ap.add_argument("-r","--reff", required=True, help="Path TO REfference")
ap.add_argument("-t","--test", required=True, help="Path to the Test File")
args=vars(ap.parse_args())


ref=cv2.imread(args["reff"])
#cv2.imshow("refference",ref)
test=cv2.imread(args["test"])
out=refResize(ref,test)
cv2.imshow("Refference",ref)
cv2.imshow("Test Image", test)
cv2.imshow("Output Image", out)
cv2.waitKey(0)
"""
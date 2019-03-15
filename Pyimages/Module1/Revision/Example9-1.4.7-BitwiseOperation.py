"""
when we used cropping we can only crop the Rectangular space suppose the region of interest is non-rectangular
to Extract this type of regions we can use bitwise operation with the masking to extract non-rectangular ROI

Bitwise operations operate in a binary manner and are represented as grayscale images. A given pixel is turned “off”
if it has a value of zero and it is turned “on” if the pixel has a value greater than zero.

bitwise operations
Bitwise Operations
    AND: A bitwise AND is true if and only if both pixels are greater than zero.
    cv2.bitwise_and(src1,src2,dst,mask)
    OR: A bitwise OR is true if either of the two pixels are greater than zero.
    cv2.bitwise_or(src1,src2,dst,mask)
    XOR: A bitwise XOR is true if and only if one of the two pixels is greater than zero, but not both.
    cv2.bitwise_xor(src1,src2,dst,mask)
    NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.
    cv2.bitwise_not(src1,dst,mask)

"""
import numpy as np
import cv2

#creating the binary Rectangle and circle canvas
canvas1=np.zeros((300,300),dtype="uint8")
cv2.rectangle(canvas1,(50,50),(250,250),255,-1)
canvas2=np.zeros((300,300),dtype="uint8")
cv2.circle(canvas2,(150,150),120,255,-1)
cv2.imshow("Rectangle",canvas1)
cv2.imshow("Circle",canvas2)
cv2.waitKey(0)

#AND Operation
And=cv2.bitwise_and(canvas1,canvas2)
cv2.imshow("And Operation",And)
cv2.waitKey(0)
#or operation
OR=cv2.bitwise_or(canvas1,canvas2)
cv2.imshow("Or Operation",OR)
cv2.waitKey(0)
#Xor oeration
XOR=cv2.bitwise_xor(canvas1,canvas2)
cv2.imshow("Xor Oeratoin",XOR)
cv2.waitKey(0)
#not operation
NOT=cv2.bitwise_not(XOR)
cv2.imshow("Not ",NOT)
cv2.waitKey(0)
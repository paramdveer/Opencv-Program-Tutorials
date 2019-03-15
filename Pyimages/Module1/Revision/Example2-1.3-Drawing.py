"""
In thsi lesson we will learn about drawing on the image basic figures and line
To create a empty canvas of given heigh anf widh

np.zeros((<height>,<width>,<numbe of channels>),dtype="<Data type >")
np.zeros((300,300,3),dtype="uint8")
cv2.line(<image>,(x1,y1),(x2,y2),<color>,Thickness,line tpe, shift)
cv2.rectangle(<image>,pt1,pt2,<color>, <thickness//-1 to fill inside, line type, shift)
cv2.circle(image, center, radius, color, <thickness//-1 to fill inside, line type, shift)

to generate a random number np.random.randint(<lowest count>,high=<highest count>)
to generate a random colour or list of 3 values np.random.randint(0, high=<highest value>, size=(<size>)).tolist()
radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))


"""
import cv2
import numpy as np
# to create a empty canvas with all the values as zero
canvas=np.zeros((300,300,3),dtype="uint8")
# draw a diagonal green line
green=(0,255,0)
pink=(153, 153, 255)
blue=(255,102,0)
white=(255,255,255)
red=(0,0,255)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.line(canvas,(0,300),(300,0),green,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

(h,w)=canvas.shape[:2]
(cX,cY)=(w//2,h//2)
#Drawing a rectange
cv2.rectangle(canvas,(100,100),(200,200),pink,2)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.rectangle(canvas,(120,120),(180,180),red,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

cv2.circle(canvas,(cX,cY),30,white,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

# to draw circle from a common center
for i in range(30,150,30):
    cv2.circle(canvas,(cX,cY),i,white,2)
    cv2.imshow("Canvas",canvas)
    cv2.waitKey(0)

for i in range(0, 25):
    # randomly generate a radius size between 5 and 200, generate a random
    # color, and then pick a random point on our canvas where the circle
    # will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

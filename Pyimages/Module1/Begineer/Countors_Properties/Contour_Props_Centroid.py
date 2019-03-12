import argparse
import numpy as np
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(a,cnts,b)=cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
clone=image.copy()
print(len(cnts))
for c in cnts:
    M=cv2.moments(c)
    Cx=int(M["m10"]/M["m00"])
    Cy=int(M["m01"]/M["m00"])
    cv2.circle(clone,(Cx,Cy),10,(0,255,0),-1)
cv2.imshow("Centroid",clone)
cv2.waitKey(0)
clone=image.copy()

#Area and perimeter Calcluation

for (i,c) in enumerate(cnts):
    #calclualte the Area and perimeter
    area=cv2.contourArea(c)
    peri=cv2.arcLength(c,True)
    print("The #{} Area{:.2f}----:Perimeter{:.2f}".format(i+1,area,peri))
    #Draw the countour outline int the original image
    cv2.drawContours(clone,[c],-1,(0,255,0),2)
    M=cv2.moments(c)
    Cx=int(M["m10"]/M["m00"])
    Cy=int(M["m01"]/M["m00"])
    cv2.putText(clone,"#{}".format(i+1),(Cx-20,Cy),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.25,(255,255,255),4)

cv2.imshow("Contours",clone)
cv2.waitKey(0)


# Bounding Boxes
for c in cnts:
    #Calcluate the starting x(left),y(Top) pooints and then width and height of rectangle that could enclose figure
    (x,y,w,h)=cv2.boundingRect(c)
    cv2.rectangle(clone,(x,y),(x+w,y+h),(0,0,255),2)

#display the image with the bpounded rectangles
cv2.imshow("Bounded Contours",clone)
cv2.waitKey(0)
clone=image.copy()

#ROtated Bounded Box
for c in cnts:
    box=cv2.minAreaRect(c)
    box=np.int0(cv2.boxPoints(box))
    cv2.drawContours(clone,[box],-1,(255,0,0),3)

cv2.imshow("Rotated Bounded Boxes",clone)
cv2.waitKey(0)
clone=image.copy()

#Minimum Enclosing Circle
for c in cnts:
    ((x,y),radius)=cv2.minEnclosingCircle(c)
    cv2.circle(clone,(int(x),int(y)),int(radius),(0,255,0),3)

cv2.imshow("Min-Enclosing-Circle",clone)
cv2.waitKey(0)
clone=image.copy()

#Fitting in Eclipse
for c in cnts:
    if len(c)>=5:
        ellipse=cv2.fitEllipse(c)
        cv2.ellipse(clone,ellipse,(255,0,0),3)
cv2.imshow("Elipses",clone)
cv2.waitKey(0)
clone=image.copy()
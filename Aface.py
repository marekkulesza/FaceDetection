import cv2
import numpy as np
 
# THIS PROJECT OPENS UP 2 IMAGES AND CHECKS IF EITHER HAVE A FACE IN IT

################################################################

# CHANGES GO HERE, DONT TOUCH ANYTHING ELSE

frameWidth = 1280 # DISPLAY WIDTH
frameHeight = 960 # DISPLAY HEIGHT

datalocation1 = "C:\\Users\\ayylmbo\\Desktop\\face1.png" # THE PATH TO THE FILE
datalocation2 = "C:\\Users\\ayylmbo\\Desktop\\dog.jpg" # THE PATH TO THE 2ND FILE

facecascadelocation = "C:\\Users\\ayylmbo\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml" # PATH TO THE CASCADE

#################################################################
 
# READ THE IMAGES
img1 = cv2.imread(datalocation1,1)
img2 = cv2.imread(datalocation2,1) 

def empty(a): #IGNORE THIS
    pass

def stackImages(scale,imgArray): #FOR STACKING THE IMAGES SIDE BY SIDE
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 
# LOAD THE CLASSIFIERS
cascade = cv2.CascadeClassifier(facecascadelocation)
faces1 = cascade.detectMultiScale(img1)
faces2 = cascade.detectMultiScale(img2)

# ADD TRACKBARS
while True:

    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in faces1:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img1,"Face!",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        roi_color = img1[y:y+h, x:x+w]
        print("Image 1 has a face!")


    for (x,y,w,h) in faces2:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img2,"Face!",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        roi_color = img2[y:y+h, x:x+w]
        print("Image 2 has a face!")

    imgStack = stackImages(0.7,([img1,img2])) # Change the int to scale the stacked images
    cv2.imshow("Are these faces?",imgStack)
    cv2.waitKey(0)
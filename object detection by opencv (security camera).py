import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame=cam.read()
    ret,frame1=cam.read()
    
    diff=cv2.absdiff(frame,frame1)
    
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    
    Blur=cv2.GaussianBlur(gray,(5,5),0)
    
    _, thresh=cv2.threshold(Blur,20,255,cv2.THRESH_BINARY)
    
    dilated=cv2.dilate(thresh,None,iterations=3)
    
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #if we want to highlight all moving object in camera we use below commented
    #line of code otherwise we will use for loop given below
    
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
   
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.PlaySound('mixkit-police-siren-us-1643.wav',winsound.SND_ASYNC)
        
    if cv2.waitKey(20)==ord('q'):
        break
    cv2.imshow('camera',frame1)

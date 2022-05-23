import pytesseract
from pytesseract import Output
import cv2
import PIL.Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

mycon=r"--psm 6--oem 3"

img=cv2.imread("10002.png")
height,weight,_=img.shape

data=pytesseract.image_to_data(img,config=mycon,output_type=Output.DICT)

amount_boxes=len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i])>40:
        (x,y,width,height)=(data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        img=cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
        img=cv2.putText(img,data['text'][i],(x,y+height+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)
    

cv2.imshow("image",img)
cv2.waitKey(0)

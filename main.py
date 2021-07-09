import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS,160)
segmentor = SelfiSegmentation(0)
fpsReader = cvzone.FPS()
##imgBg = cv2.imread("Backgrounds/1.jpg")

listImg = os.listdir("Backgrounds")
print(listImg)

imgList = []
for imPath in listImg:
    img = cv2.imread(f'Backgrounds/{imPath}')
    imgList.append(img)

print(len(imgList))

indexImg = 0


while True:
    success,img = cap.read()
    imgOut = segmentor.removeBG(img,imgList[indexImg],threshold=0.1)
    

    imgStacked = cvzone.stackImages([img,imgOut],2,1)

    fps, imgStacked = fpsReader.update(imgStacked,color = (0,0,255))
##    cv2.imshow("WebCam",img)
    cv2.imshow("WebCam Out",imgOut)
##    cv2.imshow("WebCam Stacked",imgStacked)
    key = cv2.waitKey(1)

    if key == ord('a'):
        if indexImg == 0:
            indexImg = 10
        else:
            indexImg -=1
    elif key == ord('d'):
        if indexImg == 10:
            indexImg = 0
        else:
            indexImg +=1
    elif key == ord('q'):
        break
        

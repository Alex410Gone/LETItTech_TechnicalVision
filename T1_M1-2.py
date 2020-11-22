import cv2.cv2 as cv2
import numpy as np

#Часть_1
#
#функция вывода изображения 
def show(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)

#создаем объект
res = np.full((400,600,3),(0,0,0),np.uint8)

#очень плохой код, лучше закрыть на это глаза, но главное работает :)
for x in range(400):
    for y in range(600):
        if x >= 0 and x<=100 and y>=0 and y<=100:
            res[x,y] = [255,255,255]

        if x >= 0 and x<=100 and y>=200 and y<=300:
            res[x,y] = [255,255,255]

        if x >= 0 and x<=100 and y>=400 and y<=500:
            res[x,y] = [255,255,255]

        if x >= 100 and x<=200 and y>=100 and y<=200:
            res[x,y] = [255,255,255]
        
        if x >= 100 and x<=200 and y>=300 and y<=400:
            res[x,y] = [255,255,255]

        if x >= 100 and x<=200 and y>=500 and y<=600:
            res[x,y] = [255,255,255]

        if x >= 200 and x<=300 and y>=0 and y<=100:
            res[x,y] = [255,255,255]

        if x >= 200 and x<=300 and y>=200 and y<=300:
            res[x,y] = [255,255,255]

        if x >= 200 and x<=300 and y>=400 and y<=500:
            res[x,y] = [255,255,255]

        if x >= 300 and x<=400 and y>=100 and y<=200:
            res[x,y] = [255,255,255]
        
        if x >= 300 and x<=400 and y>=300 and y<=400:
            res[x,y] = [255,255,255]

        if x >= 300 and x<=400 and y>=500 and y<=600:
            res[x,y] = [255,255,255]

#расчет втогоро изображения, где черный => синий
b,r,g = cv2.split(res)
for x in range(400):
    for y in range(600):
        if b[x,y] == 0:
            b[x,y] = 255

res_1 = cv2.merge((b,r,g))

show("Image_1", res)
show("Image_2", res_1)
cv2.waitKey(0)

#Часть_2
#
#создаем объект
res = np.full((600,600,3),(255,255,255),np.uint8)

#круг
cv2.putText(res, "Круг", (360,50),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
center = (res.shape[1]/2, res.shape[0]/2)
radius = 85
cv2.circle(res,(400,150),radius,(255,0,0),thickness=3,lineType=cv2.LINE_AA)

#прямоугольник
cv2.putText(res, "Прямоугольник", (60,530),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
pt1=(50,400)
pt2=(350,500)
cv2.rectangle(res,pt1,pt2,(0,0,255),thickness=3)

#прямая линия
cv2.putText(res, "Линия", (320,300),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
p1 = (0,0)
p2 = (res.shape[1] - 1, res.shape[0] - 1)
cv2.line(res,p1,p2,(0,255,0),thickness=3,lineType=cv2.LINE_AA)

show("Image_3", res)
cv2.waitKey(0)

#Часть_3
#
#к сожалению отстутвует камера :( поэтому писал как по примеру
cam = cv2.VideoCapture(0)
while(True):
    _, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, "22.11.2020", (320,280),cv2.FONT_ITALIC, 1, (0,0,0), thickness=3, lineType=cv2.LINE_AA)
    show("VIDEO", frame)
    if cv2.waitKey(1) == 113:
        break

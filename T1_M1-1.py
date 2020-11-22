import numpy as np
import cv2.cv2 as cv2

#функция вывода изображения 
def show(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)

#путь к изображению
IMAGE = "F:\\webpunk.jpg"

#1.Показать цветную картинку в полном размере
#
#считываем изображение
img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
#выводим в консоль длину и ширину
height = np.size(img, 0)
width = np.size(img, 1)
print("1: ", "w:", width," h:", height)
#показываем изображение
show("wImage", img)
#ждем 5сек
cv2.waitKey(5000)

#2.Показать в оттенках серого картинку в полном размере
#
#считываем изображение
img = cv2.imread(IMAGE, cv2.IMREAD_GRAYSCALE)
#выводим в консоль длину и ширину
height = np.size(img, 0)
width = np.size(img, 1)
print("2: ","w:", width," h:", height)
#показываем изображение
show("wImage", img)
#ждем 7сек
cv2.waitKey(7000)

#3.Показать цветную картинку в 2 раза меньше
#
#считываем изображение
img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
#уменьшаем размер
resize = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#выводим в консоль длину и ширину
height = np.size(resize, 0)
width = np.size(resize, 1)
print("3: ","w:", width," h:", height)
#показываем изображение
show("wImage", resize)
#ждем 9сек
cv2.waitKey(9000)

#4.Показать в оттенках серого картинку в 4 раза меньше
#
#считываем изображение
img = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
#уменьшаем размер
resize = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
#выводим в консоль длину и ширину
height = np.size(resize, 0)
width = np.size(resize, 1)
print("4: ","w:", width," h:", height)
#показываем изображение
show("wImage", resize)
#ждем 11сек
cv2.waitKey(11000)

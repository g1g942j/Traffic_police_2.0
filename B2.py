"""
pprint( cv.__version__ )erson = {"name": "Kelly", "age": 25, "city": "New york"}
print(person.get("age"))

models_data = {"BMMW": ['x6', 'm5'], "ВАЗ": ['2106','2112'], "Tesla": ['Model S','Model S Plaid']}
print(models_data["Tesla"][1])

from collections import  Counter
lists = ["a", "b", "c", "a", "c", "z"]
counts = Counter(lists)
print(counts)
"""
import cv2 as cv
print( cv.__version__ )
img = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf.png')
img1 = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf(1).png')
cv.imshow("123", img1)
print('Высота:'+str(img.shape[0]))
print('Ширина:'+str(img.shape[1]))
print('Количество каналов:'+str(img.shape[2]))
print('Высота:'+str(img1.shape[0]))
print('Ширина:'+str(img1.shape[1]))
print('Количество каналов:'+str(img1.shape[2]))
pixel = img[100, 100]
di = img1.shape
print(pixel)
print(di)

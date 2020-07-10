# from registry import DEMOANNO
#
# @DEMOANNO.hellob
# class Demo(object):
#     def __init__(self):
#         pass
#
#     def helloa(self):
#         print("hello2")
#
# if __name__ == '__main__':
#     list = []
#     for i in range (0,5):
#         str  = f'{i}'
#         list.append(str)
#     print(list)
from PIL import Image
import matplotlib.pyplot as plt

def cut(im, list, vx, vy):
    dx = vx
    dy = vy
    x1 = 0
    y1 = 0
    x2 = vx
    y2 = vy
    xNum = 1
    yNum = 1
    column = []
    while xNum <= 5:
        while yNum <= 4:
            yNum += 1
            im2 = im.crop((x1, y1, x2, y2))
            column.append(im2)
            y1 = y1 + dy
            y2 = y1 + vy
        yNum = 1
        xNum += 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy
        list.append(column)
        column = []

if __name__ == '__main__':
    im = Image.open("/Users/yangwenbo/Desktop/Image_20200616090411492.jpg")
    list = []
    cut(im, list, 1094, 912)
    print(list)

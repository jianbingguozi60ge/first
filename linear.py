# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
def up(route):
    # 读取原始图像
    img = cv2.imread(route)

    # 图像灰度转换
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 获取图像高度和宽度
    height = grayImage.shape[0]
    width = grayImage.shape[1]

    # 创建一幅图像
    result = np.zeros((height, width), np.uint8)

    # 图像灰度上移变换 DB=DA+50
    for i in range(height):
        for j in range(width):

            if (int(grayImage[i, j] + 50) > 255):
                gray = 255
            else:
                gray = int(grayImage[i, j] + 50)

            result[i, j] = np.uint8(gray)

    return result

def enhance(route):

    img = cv2.imread(route)

    # 图像灰度转换
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 获取图像高度和宽度
    height = grayImage.shape[0]
    width = grayImage.shape[1]

    # 创建一幅图像
    result = np.zeros((height, width), np.uint8)

    # 图像对比度减弱变换 DB=DA*0.8
    for i in range(height):
        for j in range(width):
            gray = int(grayImage[i, j] * 1.2)
            result[i, j] = np.uint8(gray)

    return result

def weak(route):

    # 读取原始图像
    img = cv2.imread(route)

    # 图像灰度转换
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 获取图像高度和宽度
    height = grayImage.shape[0]
    width = grayImage.shape[1]

    # 创建一幅图像
    result = np.zeros((height, width), np.uint8)

    # 图像对比度减弱变换 DB=DA*0.8
    for i in range(height):
        for j in range(width):
            gray = int(grayImage[i, j] * 0.8)
            result[i, j] = np.uint8(gray)

    return result


route = 'C:\\Users\\root\Desktop\pic\pic2.jpg'
image = cv2.imread(route)
image_up = up(route)
image_enhance = enhance(route)
image_weak = weak(route)
images = [image,image_up,image_enhance,image_weak]
titles = ['image','image_up','image_enhance','image_weak']
for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])
plt.show()

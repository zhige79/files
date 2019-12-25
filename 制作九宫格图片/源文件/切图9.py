# -*- coding:utf-8 -*-
from PIL import Image
import sys
import time


def fill_image(image):
    width, height = image.size
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    if  width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return image


def cut_image(image):
    width, height = image.size
    item_width = int(width/3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j*item_width, i*item_width, (j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list


def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('.2'+str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    fire_path = "1.jpg"
    image = Image.open(fire_path)
    image = fill_image(image)
    print("正在生成，请稍后！")
    image_list = cut_image(image)
    image_list = cut_image(image)
    print("正在保存！")
    save_images(image_list)
    print("自动退出。。。")
    time.sleep(1)

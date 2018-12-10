import numpy as np
import cv2
from matplotlib import pyplot as plt
import time
import os
from PIL import Image
import copy

FILTER_SIZE = 40
COMPRESS_RATE = 0.25

colors = {"red": (255, 0, 0),
          "green": (0, 128, 0),
          "blue": (135,206,235),
          "white": (255, 255, 255),
          "black": (0,0,0),
          "yellow": (255, 255, 0),
          "purple": (128, 0, 128)}


def sqt_dif(c1, c2):
    return (c1-c2)**2


def color_distance(img_1, img_2):
    img_1 = cv2.resize(img_1, (FILTER_SIZE*COMPRESS_RATE, FILTER_SIZE*COMPRESS_RATE)).flatten()
    img_2 = cv2.resize(img_2, (FILTER_SIZE*COMPRESS_RATE, FILTER_SIZE*COMPRESS_RATE)).flatten()
    dis = 0
    for pix_pair in list(zip(img_1, img_2)):
        dis += sqt_dif(pix_pair[0], pix_pair[1])
    return dis

def process_whole_folder(path):
    tiles = []
    count = 0
    for file in os.listdir(path):
        print("Processed: " + str(count))
        print("All: " + str(len(os.listdir(path))))
        p = path + "/" + file
        curr_img = cv2.imread(p)
        if curr_img is None or len(curr_img) == 0:
            continue
        resized_image = cv2.resize(curr_img, (FILTER_SIZE, FILTER_SIZE))
        tiles.append(resized_image)
        count += 1
    return tiles

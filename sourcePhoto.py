import numpy as np
import cv2
from matplotlib import pyplot as plt
import time
import os
from PIL import Image

colors = {"red": (255, 0, 0),
          "green": (0, 128, 0),
          "blue": (135,206,235),
          "white": (255, 255, 255),
          "black": (0,0,0),
          "yellow": (255, 255, 0),
          "purple": (128, 0, 128)}


def sqt_dif(c1, c2):
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2


def color_distance(img_1, img_2):
    img_1 = np.flatten(cv2.resize(img_1, (10, 10)))
    img_2 = np.flatten(cv2.resize(img_2, (10, 10)))
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
        curr_img = Image.open(p)
        resized_image = curr_img.resize((20, 20), Image.ANTIALIAS)
        tile = np.array(resized_image)
        tiles.append(tiles)
        count += 1
    return tiles

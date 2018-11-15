import numpy as np
import cv2
from matplotlib import pyplot as plt
import time
from sourcePhoto import *

FILTER_SIZE = 20
TARGET_IMAGE_SIZE = 4000

def process_whole(img):
    img = cv2.resize(img, (TARGET_IMAGE_SIZE, TARGET_IMAGE_SIZE))
    return img

def apply_filter(img, tiles):
    for row in range(0, TARGET_IMAGE_SIZE, FILTER_SIZE):
        for col in range(0, TARGET_IMAGE_SIZE, FILTER_SIZE):
            print("CurrPos:")
            print("Row:" + str(row))
            print("Col:" + str(col))
            curr_input = np.empty((20,20, 3))
            for ro in range(0, 20):
                for co in range(0, 20):
                    curr_input[ro][co] = img[row+ro][col+co]
            clo_dis = 0
            clo_img = None
            np.random.shuffle(tiles)
            for tile in tiles:
                curr_dis = color_distance(curr_input, tile)
                if clo_img is None or curr_dis < clo_dis:
                    clo_dis = curr_dis
                    for r in range(0, 20):
                        for c in range(0,20):
                            img[row+r][col+c] = tile[r][c]

tiles = process_whole_folder("/Volumes/Extreme 500/FrankZhou's/MoS")
img = process_whole(cv2.imread("/Users/intermediatephoto/Desktop/DSC_0203.jpg"))
apply_filter(img, tiles)
print(img)


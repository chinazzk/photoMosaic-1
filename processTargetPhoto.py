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
            curr_input = img[row:row+20][col:col+20]
            clo_dis = 0
            clo_img = None
            np.random.shuffle(tiles)
            for tile in tiles:
                curr_dis = color_distance(curr_input, tile)
                if clo_img == None or curr_dis < clo_dis:
                    clo_dis = curr_dis
                    img[row:row + 20][col:col + 20] = tiles

tiles = process_whole_folder("/Volumes/Extreme 500/FrankZhou's/MoS")
img = process_whole("/Users/intermediatephoto/Desktop/DSC_0203.jpg")
apply_filter(img, tiles)
cv2.imshow(img)


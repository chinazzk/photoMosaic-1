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
    count = 0
    for row in range(0, TARGET_IMAGE_SIZE, FILTER_SIZE):
        for col in range(0, TARGET_IMAGE_SIZE, FILTER_SIZE):
            count +=1
            start = time.time()
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
                    clo_img = tile
            for r in range(0, 20):
                for c in range(0,20):
                    img[row+r][col+c] = clo_img[r][c]
            if count % 100 ==0:
                print()
                print("CurrPos:")
                print("Row:" + str(row))
                print("Col:" + str(col))
                print("Closest Distance: " + str(clo_dis))
                end = time.time()
                print("Estimate Overall Time: " + str((end-start)*40000) + " second")
                print("Time Used: " + str(end-start_apply_filter) + " second")
                print("Time Remaining: " + str((end-start)*40000 - (end-start_apply_filter)))


tiles = process_whole_folder("/Users/frank/Documents/GitHub/photoMosaic/Mos")
img = process_whole(cv2.imread("/Users/frank/Documents/GitHub/photoMosaic/IMG_3328.JPG"))
start_apply_filter = time.time()
apply_filter(img, tiles)
np.save("result", img)
print(img)
plt.imshow(img)
plt.show()

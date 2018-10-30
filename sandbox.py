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

img = Image.open("/Users/intermediatephoto/Desktop/DSC_0011.jpg")

start = time.time()
resized_image = img.resize((50, 50), Image.ANTIALIAS)

resized_image =np.asarray(resized_image)

up_left = resized_image[0:10, 0:10]
up_right = resized_image[0:10, 10:20]
down_left = resized_image[10:20, 0:10]
down_right = resized_image[10:20, 10:20]

def sqt_dif(c1, c2):
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2

count = [0 for i in range(7)]
for row in up_left:
    for pix in row:
        diff = []
        for key in colors:
            diff.append(sqt_dif(pix, colors[key]))
        major = diff.index(min(diff))
        count[major] += 1

plt.imshow(resized_image)
im = Image.fromarray(resized_image)
im.save("1.jpg")
plt.show()
print(count)
end = time.time()
print(end-start)